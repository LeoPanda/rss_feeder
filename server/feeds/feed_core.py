import requests
import feedgenerator
from bs4 import BeautifulSoup
from flask import Response


class FeedCore():
    # Web scraping & feed makerの親クラス
    CDATA_TEMPLATE = '<![CDATA[<img src="{}"><br><br><a href="{}">{}</a>]]>'
    SITE_URL = ''
    TITLE = ''
    SELECTOR = ''

    def do_feed(self, path, title):
        # feedの実行
        feed_items = self.get_feed_items(self.SITE_URL+path)
        feed = self.__get_feed(self.TITLE+title,
                               self.SITE_URL, "", feed_items)
        return Response(str(feed.writeString('UTF-8')), mimetype='application/xml')

    def get_feed_items(self, req):
        # feed itemの生成
        pass

    def __get_feed(self, title, link, description, feed_items) -> feedgenerator.Rss201rev2Feed:
        # rss feedを生成する
        feed = feedgenerator.Rss201rev2Feed(
            title=title, link=link, description=description)
        for item in feed_items:
            feed.add_item(
                title=item.title,
                link=item.link,
                description=item.description,
                pubdate=item.pubdate
            )
        return feed

    def extract_feed_items(self, req, limit=None):
        # feed要素を抽出するデコレータ
        def decolator(func) -> list:
            res = requests.get(req)
            soup = BeautifulSoup(res.text, 'html.parser')
            elements = soup.select(self.SELECTOR)
            elements = elements[:limit] if limit else elements
            items = []
            for element in elements:
                item = func(element)
                if item is not None:
                    items.append(item)
            return items
        return decolator

    def get_deep_element(self, req, selector):
        # リンク先をたどってselectorで指定したエレメントを取得する
        res = requests.get(req)
        soup = BeautifulSoup(res.text, 'html.parser')
        return soup.select_one(selector)
