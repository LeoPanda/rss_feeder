from datetime import datetime


from datetime import datetime


class FeedItem:
    # rss feed item　単体格納用クラス
    title = None
    link = None
    description = None
    pubdate = None

    def __init__(self, title: str, link: str, description: str, pubdate: datetime):
        self.title = title
        self.link = link
        self.description = description
        self.pubdate = pubdate
