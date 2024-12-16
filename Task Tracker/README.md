# Let me explain the key components of the solution:

## [TaskTracker cli](https://roadmap.sh/projects/task-tracker)

## TaskTracker Class:

- Manages task operations (add, update, delete, mark status)
- Handles JSON file interactions
- Generates unique task IDs
- Tracks creation and update timestamps


## Command-line Interface:

- Supports all required operations
- Robust error handling
- Validates input arguments
- Provides user-friendly feedback


# File Handling:

- Uses native Python json and os modules
- Creates tasks.json if it doesn't exist
- Gracefully handles file reading/writing errors



## How to Use:

- Save the script as task-cli.py
- Make it executable: chmod +x task-cli.py
- Run commands like:

1. ./task-cli.py add "Buy groceries"
2. ./task-cli.py add "Buy groceries2"
3. ./task-cli.py list
4. ./task-cli.py mark-in-progress 1
5. ./task-cli.py mark-done 1
6. ./task-cli.py delete 1