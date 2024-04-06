# Process Monitor Script

This script monitors a specified process and performs tasks when the process starts and finishes. When the process starts, it pulls the latest files from a Git repository. When the process finishes, it adds any new or modified files to the Git repository, commits the changes, and pushes the commit to the remote repository.

## Usage

1. Install the required Python packages:

```bash
pip install psutil
```

2. Run the script:

```bash
python main.py
```

The script will continuously monitor the specified process and perform the defined tasks.

## Constants

- `APP_NAME`: The name of the process to monitor. In this case, it's set to "Obsidian".

## Dependencies

- `psutil`: Used for process monitoring and management.
- `subprocess`: Used for executing Git commands.
- `datetime`: Used for getting the current date for the commit message.

## Note

Make sure you have Git installed and configured on your system for the Git commands to work properly.