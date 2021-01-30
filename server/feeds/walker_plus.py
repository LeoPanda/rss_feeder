# walker plus用feed set
from server.feeds.feed_core import FeedCore
from server.models.feed_item import FeedItem
from server.feeds.date_getter import get_datetime


class WalkerPlus(FeedCore):

    def __init__(self) -> None:
        self.SITE_URL = 'https://www.walkerplus.com'
        self.TITLE = "Walker Plus"
        self.SELECTOR = 'div.m-mainlist > div > ul > li'

    def get_feed_items(self, req):
        # フィードするアイテムを生成する
        @self.extract_feed_items(req)
        def scraper(element):
            # タイトル
            title_element = element.find("a", class_="m-newslist__ttl")
            title = title_element.text if title_element else ""
            # リンク
            link = self.SITE_URL + \
                title_element["href"] if title_element else ""
            # 画像
            img_element = element.find("img")
            img = "https:" + img_element["src"] if img_element else ""
            # 概要
            description_element = element.find(
                "div", class_="m-newslist__info")
            description = self.CDATA_TEMPLATE.format(
                img, link, description_element.text) if description_element else ""
            # 日付
            date_element = element.find("p", class_="m-newslist__date")
            date_string = date_element.text if date_element else ""

            return FeedItem(
                title=title,
                link=link,
                description=description,
                pubdate=get_datetime(date_string)
            )
        return scraper
