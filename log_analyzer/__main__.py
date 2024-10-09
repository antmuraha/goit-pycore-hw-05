import sys
from format import display_level_detail, display_log_counts
import load_logs as lib


def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
        level = None
        logs = lib.load_logs(path)

        if not logs:
            return

        counts = lib.count_logs_by_level(logs)
        display_log_counts(counts)

        if len(sys.argv) == 3:
            level = sys.argv[2]

        if level:
            display_level_detail(level, lib.filter_logs_by_level(logs, level))

    else:
        print("No arguments were passed.")


if __name__ == "__main__":
    main()
