from datetime import datetime, timedelta
from typing import Tuple

def is_later(today: str, yesterday: str) -> bool:
    return datetime.strptime(today, "%Y-%m-%d %H:%M:%S") - datetime.strptime(yesterday, "%Y-%m-%d %H:%M:%S") > timedelta(hours=24)
    
def is_MorTimeinRange(early_time: int, late_time: int, now_time: datetime) -> bool:
    '''
        判断早安时间是否在范围内
        - early_time: 较早的开始时间
        - late_time: 较晚的结束时间
    '''
    pass_time = now_time - datetime(now_time.year, now_time.month, now_time.day, 0, 0, 0)

    return timedelta(hours=early_time) < pass_time < timedelta(hours=late_time)

def is_NigTimeinRange(early_time: int, late_time: int, now_time: datetime) -> bool:
    '''
        判断晚安时间是否在范围内，注意次日判断
        - early_time: 较早的开始时间
        - late_time: 较晚的结束时间
    '''
    pass_time = now_time - datetime(now_time.year, now_time.month, now_time.day, 0, 0, 0)
    
    return pass_time > timedelta(hours=early_time) or pass_time < timedelta(hours=late_time)

def is_TimeinInterval(_datetime: str, now_time: datetime, interval: int) -> bool:
    '''
        1. 判断是否多次早安，上次早安时间和现在时间相差不超过interval，True则成立。此时，_datetime = good_morning_time
        2. 判断是否超级亢奋，上次晚安时间和现在时间相差不超过interval，True则成立。此时，_datetime = good_night_time
        3. 判断是否优质睡眠，上次晚安时间和现在时间相差不超过interval，True则成立
        4. 判断是否深度睡眠，上次早安时间和现在时间相差不超过interval，True则成立
        5. 判断早安是否隔日(interval=24)，例如存在此情况：
            在01-01 23:00:00 晚安
            在01-03 07:00:00 早安
            True: 则未隔日
    '''
    return now_time - datetime.strptime(_datetime, '%Y-%m-%d %H:%M:%S') < timedelta(hours=interval)

def get_time_tuple(time_interval: timedelta) -> Tuple[int, int, int, int]:
    secs: int = time_interval.seconds()
    days: int = secs // (3600 * 24)
    hours: int = int((secs - days * 3600 * 24) // 3600)
    minutes: int = int((secs - days * 3600 * 24 - hours * 3600) // 60)
    seconds: int = int(secs - days * 3600 * 24 - hours * 3600 - minutes * 60)
    
    return days, hours, minutes, seconds

#TODO: A cimpatible transfer from old morning data to new version's