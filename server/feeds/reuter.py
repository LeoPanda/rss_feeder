# ロイター用feed set
from server.feeds.feed_core import FeedCore
from server.models.feed_item import FeedItem
from server.feeds.date_getter import get_datetime

MAIN_SELECTOR = "div.moduleBody>div.feature"
OPINION_SELECTOR = "div.module.inline>div.moduleBody>div.feature"


class Reuter(FeedCore):

    def __init__(self, is_opinion=False) -> None:
        self.SITE_URL = 'https://jp.reuters.com'
        self.TITLE = "ロイター"
        self.SELECTOR = OPINION_SELECTOR if is_opinion else MAIN_SELECTOR

    def get_feed_items(self, req):
        # フィードするアイテムを生成する
        @self.extract_feed_items(req)
        def scraper(element):
            # タイトル
            title_element = element.find("h2")
            title = title_element.text if title_element else ""
            # リンク
            link_element = element.find("a")
            link = self.SITE_URL+link_element["href"] if link_element else ""
            # 画像
            img_element = element.find("img")
            img = img_element["src"] if img_element else ""
            # 概要
            description_element = element.find("p")
            description = self.CDATA_TEMPLATE.format(
                img, link, description_element.text) if description_element else ""
            # 日付
            date_element = element.find("span", class_="timestamp")
            date_string = date_element.text if date_element else ""

            return FeedItem(
                title=title,
                link=link,
                description=description,
                pubdate=get_datetime(date_string)
            )
        return scraper
