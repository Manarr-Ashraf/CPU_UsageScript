# CPU Usage Logger

This Python script monitors the CPU usage of the system and logs it to a file with timestamps. It captures the CPU usage percentage for all CPU cores every 5 seconds, calculates the average usage, and appends the data to a log file. The script runs continuously until manually stopped by the user.

## Features
- Logs CPU usage percentage in real-time.
- Records the date and time for each log entry.
- Automatically handles user interruptions (`Ctrl + C`) gracefully.

## Requirements
- Python 3.x
- The `psutil` library

## Installation

1. Install Python 3.x from the official website: [Python.org](https://www.python.org/downloads/)
2. Install the required `psutil` library using `pip`:

   ```bash
   pip install psutil

## Usage

1. **Clone or download** the script to your local machine.
2. **Run the script using Python**. In your terminal or command prompt, navigate to the directory containing the script and execute:

   ```bash
   python pythonScript_CPU-Usage.py
3. **Check the log file** named log_file.txt in the same directory
4. **Stop the script** by pressing **Ctrl + C** in the terminal or command prompt

## Example Output

The log file (`log_file.txt`) will contain entries in the following format:

![Example Output](https://github.com/user-attachments/assets/19aa5322-b9df-431c-bfd5-0f6cc1ff98b4)




