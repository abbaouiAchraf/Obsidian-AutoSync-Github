import psutil
import time
import subprocess
from datetime import date


def monitor_process(process_name):
    """
    Monitor a specific process and perform tasks when the process starts and finishes.

    Args:
        process_name (str): The name of the process to monitor.
    """
    while True:
        for process in psutil.process_iter(['name']):
            if process_name in process.info['name']:
                print(f"Process '{rpocess_name}' detected. Performing task...")
                perform_task_when_detected()

                while process.is_running():
                    time.sleep(1)

                print(f"Process '{process_name}' finished. Performing another task...")
                perform_task_when_finished()

        time.sleep(1)


def perform_task_when_detected():
    """
    Perform a task when the monitored process is detected.
    """
    try:
        subprocess.check_call(['git', 'pull', 'origin', 'main'])
        print("Files pulled successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Unable to pull files. {e}")


def clean_file_name(file_name: bytes) -> str:
    """
    Clean the file name by removing the b' prefix and ' from it.

    Args:
        file_name (str): The file name to clean.

    Returns:
        str: The cleaned file name.
    """
    return str(file_name[2:-1])


def perform_task_when_finished():
    """
    Perform tasks when the monitored process finishes.
    """
    try:
        output = subprocess.check_output(['git', 'ls-files', '--others', '--exclude-standard'],
                                         stderr=subprocess.STDOUT)
        if not output:
            print("No files to commit.")
            return

        files_list = output.splitlines()
        for file in files_list:
            print(f"File to be added: {file}")
            subprocess.check_call(['git', 'add', clean_file_name(file)])
        subprocess.check_call(['git', 'commit', '-m', f'Commit of: {date.today()}'])
        subprocess.check_call(['git', 'push', 'origin', 'main'])
        print("Files added, committed, and pushed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Unable to add, commit, or push files. {e}")


if __name__ == "__main__":
    # Constants
    APP_NAME = "Obsidian"
    # Monitor the process
    monitor_process(APP_NAME)
