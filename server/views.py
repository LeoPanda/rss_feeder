from flask import Blueprint
from server.feeds.tokyo_np import TokyoNp
from server.feeds.reuter import Reuter
from server.feeds.jiji import Jiji
from server.feeds.kyotopi import Kyotopi
from server.feeds.walker_plus import WalkerPlus

root = Blueprint('root', __name__)

tokyo_np = TokyoNp()
reuter = Reuter()
reuter_for_opinion = Reuter(is_opinion=True)
jiji = Jiji()
kyotopi = Kyotopi()
walker_plus = WalkerPlus()


@root.route('/feed/tokyo-np/main')
# 東京新聞 主要
def tokyonp_main():
    return tokyo_np.do_feed('/n/main/', ':主要')


@root.route('/feed/tokyo-np/column')
# 東京新聞　社説・コラム
def tokyonp_column():
    return tokyo_np.do_feed('/n/column/', ':社説・コラム')


@root.route('/feed/tokyo-np/culture')
# 東京新聞　文化・芸能
def tokyonp_culture():
    return tokyo_np.do_feed('/f/culture/', ':文化・芸能')


@root.route('/feed/reuter/main')
# ロイター　トップニュース
def reuter_main():
    return reuter.do_feed('/pNewsnews/to', ':トップニュース')


@root.route('/feed/reuter/life')
# ロイター　ライフ
def reuter_life():
    return reuter.do_feed('/life', ':ライフ')


@root.route('/feed/reuter/opinion')
# ロイター　コラム
def reuter_opinion():
    return reuter_for_opinion.do_feed('/opinion', ':コラム')


@root.route('/feed/jiji/main')
# 時事通信
def jiji_main():
    return jiji.do_feed('/jc/list?g=news', ':主要')


@root.route('/feed/kyotopi/main')
# kyotopi
def kyotopi_main():
    return kyotopi.do_feed('', '')


@root.route('/feed/walkerplus/main')
# Wolker Plus　関西
def walkerplus_main():
    return walker_plus.do_feed('/article_list/ar0700/', ':関西')
