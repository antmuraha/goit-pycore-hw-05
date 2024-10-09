
from time import strptime
import constants


def parse_log_line(index: int, line: str) -> str:
    parts = line.split(" ")
    date = prepare_date(index, parts[0])
    time = prepare_time(index, parts[1])
    level = prepare_level(index, parts[2])
    message = " ".join(parts[3:]).strip()
    return {
        "line": index,
        "date": date,
        "time": time,
        "level": level,
        "message": message
    }


def prepare_date(index: int, date: str) -> str:
    try:
        strptime(date, "%Y-%m-%d")
    except:
        raise ExceptionDate(index)
    return date


def prepare_time(index: int, time: str) -> str:
    try:
        strptime(time, "%H:%M:%S")
    except:
        raise ExceptionTime(index)
    return time


def prepare_level(index: int, level: str) -> str:
    try:
        constants.LEVELS.index(level)
    except:
        raise ExceptionLevel(index)

    return level


class ExceptionDate(Exception):
    def __init__(self, line: int) -> None:
        super().__init__(f"The Date in line '{line}' is incorrect")


class ExceptionTime(Exception):
    def __init__(self, line: int) -> None:
        super().__init__(f"The Time in line '{line}' is incorrect")


class ExceptionLevel(Exception):
    def __init__(self, line: int) -> None:
        super().__init__(f"The Level in line '{line}' is incorrect")
