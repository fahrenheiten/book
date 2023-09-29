import os
import zipfile
from datetime import datetime, timedelta


def archive_logs(directory, age_days=30):
    """
    Archives log files older than a specified number of days.

    Parameters:
    - directory (str): The directory to search for log files.
    - age_days (int, optional): The age of log files to archive. Defaults to 30 days.

    Returns:
    - None
    """

    # Calculate the cutoff date; logs older than this date will be archived
    cutoff_date = datetime.now() - timedelta(days=age_days)

    # List all files in the directory
    files_in_directory = os.listdir(directory)

    # Filter the files that are older than the cutoff date
    old_logs = []
    for file in files_in_directory:
        file_path = os.path.join(directory, file)
        # Ensure the file is indeed a file and not a subdirectory
        if os.path.isfile(file_path):
            file_creation_date = datetime.fromtimestamp(os.path.getctime(file_path))
            # Check if the file ends with .log and if it's older than the cutoff date
            if file.endswith(".log") and file_creation_date < cutoff_date:
                old_logs.append(file_path)

    # Archive the old logs into a zipfile
    if old_logs:
        archive_name = os.path.join(directory, f"logs_{datetime.now().strftime('%Y%m%d%H%M%S')}.zip")
        with zipfile.ZipFile(archive_name, 'w') as archive:
            for log in old_logs:
                archive.write(log, os.path.basename(log))
                os.remove(log)  # Remove the original log file after archiving

        print(f"Archived {len(old_logs)} log files to {archive_name}")
    else:
        print("No old log files found to archive.")


# Example usage
if __name__ == "__main__":
    log_directory = input("Enter the path to the directory containing log files: ")
    days_old = int(input("Archive logs older than how many days? (default is 30 days): ") or 30)
    archive_logs(log_directory, days_old)
