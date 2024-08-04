import sys
from typing import List, Dict, Callable, Optional, Union

def parse_log_line(line: str) -> Dict[str, str]:
    """
    Parses a single log line into its components: date, time, level, and message.
    
    :param line: A single line from the log file.
    :return: A dictionary with the date, time, level, and message.
    """
    parts = line.split(maxsplit=3)
    if len(parts) < 4:
        return {}
    return {
        "date": parts[0],
        "time": parts[1],
        "level": parts[2],
        "message": parts[3]
    }

def load_logs(file_path: str) -> List[Dict[str, str]]:
    """
    Loads and parses logs from the specified file.
    
    :param file_path: Path to the log file.
    :return: A list of dictionaries containing parsed log entries.
    """
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                log_entry = parse_log_line(line.strip())
                if log_entry:
                    logs.append(log_entry)
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        sys.exit(1)
    return logs

def filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[Dict[str, str]]:
    """
    Filters log entries by the specified logging level.
    
    :param logs: List of log entries.
    :param level: The log level to filter by (e.g., 'ERROR').
    :return: A list of filtered log entries.
    """
    return [log for log in logs if log["level"].upper() == level.upper()]

def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    """
    Counts the number of log entries for each logging level.
    
    :param logs: List of log entries.
    :return: A dictionary with the count of log entries for each level.
    """
    levels = ["INFO", "DEBUG", "ERROR", "WARNING"]
    counts = {level: 0 for level in levels}
    for log in logs:
        level = log["level"].upper()
        if level in counts:
            counts[level] += 1
    return counts

def display_log_counts(counts: Dict[str, int]) -> None:
    """
    Displays the counts of log entries for each logging level in a formatted table.
    
    :param counts: A dictionary with the counts of log entries for each level.
    """
    print(f"{'Log Level':<15} | {'Count':<5}")
    print("-" * 22)
    for level, count in counts.items():
        print(f"{level:<15} | {count:<5}")

def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python main.py <log_file_path> [log_level]")
        sys.exit(1)

    file_path = sys.argv[1]
    log_level = sys.argv[2].upper() if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level)
        if filtered_logs:
            print(f"\nDetails for level '{log_level}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print(f"No logs found for level '{log_level}'.")

if __name__ == "__main__":
    main()