def display_log_counts(counts: dict):
    """
    Output logs formatting as an example:

    ```
    Log level        | Quantity  
    ------------------------------
    INFO             | 4         
    DEBUG            | 3         
    ERROR            | 2         
    WARNING          | 1         
    ```
    """
    print(f"{'Log level':<17}| {'Quantity':<10}")
    print("-" * 30)
    for level in counts:
        count = counts.get(level)
        print(f"{level:<17}| {count:<10}")


def display_level_detail(level: str, logs: list):
    """
    Formatting target-level output logs as an example:

    ```
    Log details for the level 'debug':
    2024-01-22 08:45:23 - Attempting to connect to the database.
    2024-01-22 11:05:00 - Starting data backup process.
    2024-01-22 12:45:05 - Checking system health.     
    ```
    """

    if not len(logs):
        print(f"\nLogs for the level '{level}' is empty.")
        return

    print(f"\nLog details for the level '{level}':")
    for log in logs:
        date = log.get("date")
        time = log.get("time")
        message = log.get("message")
        print(f"{date} {time} - {message}")
