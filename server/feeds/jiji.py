# 時事通信用feed set
from server.feeds.feed_core import FeedCore
from server.models.feed_item import FeedItem
from server.feeds.date_getter import get_datetime


class Jiji(FeedCore):

    IMG_SELECTOR = "#Main > div.MainInner.Individual > article > div.ArticleText.clearfix > div > figure > a > img"

    def __init__(self) -> None:
        self.SITE_URL = 'https://www.jiji.com'
        self.TITLE = "時事通信"
        self.SELECTOR = 'div.ArticleListMain > ul.LinkList > li'

    def get_feed_items(self, req):
        # フィードするアイテムを生成する
        @self.extract_feed_items(req, limit=10)
        def scraper(element):
            # タイトル
            title_element = element.find("a")
            title = title_element.text if title_element else ""
            # リンク
            link = self.SITE_URL + \
                title_element["href"] if title_element else ""
            # 画像
            img_element = self.get_deep_element(link, self.IMG_SELECTOR) if element.find(
                "span", class_="PhotoIcon") else None
            img = self.SITE_URL + img_element["src"] if img_element else ""
            # 概要
            description = self.CDATA_TEMPLATE.format(
                img, link, title) if title_element else ""
            # 日付
            date_element = element.find("span")
            date_string = date_element.text if date_element else ""

            return FeedItem(
                title=title,
                link=link,
                description=description,
                pubdate=get_datetime(date_string)
            )
        return scraper
