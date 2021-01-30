#　文字列をdate objectに変換する
import re
from datetime import datetime, timezone, timedelta

YEAR_PATTERN = r'.{0,}?((?P<year>\d{0,})[年|/]|.{0,}?)(?P<month>\d+)[月|/]\D{0,}(?P<day>\d+)'
TIME_PATTERN = r'.{0,}?(?P<hour>\d+):(?P<minute>\d+)[^aApPmM.]{0,}(?P<ampm>[aApPmM.]{0,})'


def get_datetime(string, year_pattern=YEAR_PATTERN, time_pattern=TIME_PATTERN) -> datetime:
    #　文字列をdate objectに変換する
    dict = {}
    dict = add_matched_to_dict(add_matched_to_dict(
        dict, string, year_pattern), string, time_pattern)

    now = datetime.now()

    year = int(str(dict.get('year'))) if dict.get('year') else now.year
    month = int(str(dict.get('month'))) if dict.get('month') else now.month
    day = int(str(dict.get('day'))) if dict.get('day') else now.day
    hour = int(str(dict.get('hour'))) if dict.get('hour') else now.hour
    is_pm = ('p' in dict.get('ampm').lower()) if dict.get('ampm') else False
    hour = hour + 12 if (is_pm and hour < 12) else hour
    minute = int(str(dict.get('minute'))) if dict.get('minute') else now.minute

    return datetime(year, month, day, hour=hour, minute=minute).astimezone(timezone(timedelta(hours=+9)))


def add_matched_to_dict(dict, string, pattern):
    # パターンにマッチしたキーワードを辞書に登録する
    match = re.match(pattern, string)
    if match:
        dict.update(match.groupdict())
    return dict
