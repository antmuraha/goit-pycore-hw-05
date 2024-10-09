
import typing
from pathlib import Path
import prepare


# Define the type for a single log line
class LogLine(typing.TypedDict):
    line: int
    date: str
    time: str
    level: str
    message: str


# # Define the type for a list
LogList = typing.List[LogLine]


def load_logs(path: str) -> LogList:
    logs: LogList = []
    file = Path(path)

    if not file.exists():
        print(f"[ERROR] File {file.absolute()} not exist")
        return None

    with open(file.absolute(), encoding="utf-8") as content:
        for index, line in enumerate(content.readlines()):
            if line:
                try:
                    log_line = prepare.parse_log_line(index + 1, line)
                    logs.append(log_line)

                except prepare.ExceptionDate as e:
                    print(f"[ERROR] {str(e)}")
                except prepare.ExceptionTime as e:
                    print(f"[ERROR] {str(e)}")
                except prepare.ExceptionLevel as e:
                    print(f"[ERROR] {str(e)}")
                except Exception as e:
                    print(f"[ERROR] Line '{index + 1}'. {str(e)}")
            else:
                print(
                    f"[INFO] Line {index + 1} is empty")

    return logs


def filter_logs_by_level(logs: LogList, level: str) -> LogList:
    return list(filter(lambda item: item.get("level").lower() == level.lower(), logs))


def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for line in logs:
        level = line.get("level")
        if counts.get(level):
            counts[level] += 1
        else:
            counts[level] = 1
    return counts
