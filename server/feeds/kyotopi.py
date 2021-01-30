# 東京新聞用feed set
from server.feeds.feed_core import FeedCore
from server.models.feed_item import FeedItem
from server.feeds.date_getter import get_datetime


class Kyotopi(FeedCore):

    DATE_SELECTOR = "#sb-site > div > div > div.col.col-sm-8.content-left > div > div.article-header > div.date"

    def __init__(self) -> None:
        self.SITE_URL = 'https://kyotopi.jp'
        self.TITLE = "kyotopi"
        self.SELECTOR = 'div.list-group>div.list-group-item'

    def get_feed_items(self, req):
        # フィードするアイテムを生成する
        @self.extract_feed_items(req, limit=8)
        def scraper(element):
            # タイトル
            title_element = element.find(
                "h4", class_="list-group-item-heading")
            title = title_element.text if title_element else ""
            # リンク
            link_element = element.find("a")
            link = self.SITE_URL + \
                link_element["href"] if link_element else ""
            # 画像
            img_element = element.find("img")
            img = img_element["src"] if img_element else ""
            # 概要
            description_element = element.find(
                "div", class_="list-group-item-text")
            description = self.CDATA_TEMPLATE.format(
                img, link, description_element.text.lstrip()) if description_element else ""
            # 日付
            date_element = self.get_deep_element(link, self.DATE_SELECTOR)
            date_string = date_element.text if date_element else ""

            return FeedItem(
                title=title,
                link=link,
                description=description,
                pubdate=get_datetime(date_string)
            )
        return scraper
