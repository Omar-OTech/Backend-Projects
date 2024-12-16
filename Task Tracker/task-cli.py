#!/usr/bin/env python3

import json
import os
import sys
from datetime import datetime

class TaskTracker:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from JSON file or create a new file if it doesn't exist."""
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except(json.JSONDecodeError, IOError):
            return []
    
    def save_tasks(self):
        """Save tasks to JSON file."""
        try:
            with open(self.filename, "w") as f:
                json.dump(self.tasks, f, indent=2)
        except IOError as e:
            print(f"Error saving tasks: {e}")
            sys.exit(1)
    
    def add_task(self, description):
        """Add a new task to the list."""
        # Generate a unique ID (max of existing IDs + 1)
        task_id = max([task["id"] for task in self.tasks], default=0) + 1
        # Create task object
        new_task = {
            'id': task_id,
            'description': description,
            'status': 'To Do',
            'createdAt': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'updatedAt': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Task '{description}' added successfully.")
        print(f"Task added successfully (ID: {task_id})")
    
    def update_task(self, task_id, new_description):
        """Update an existing task in the list."""
        for task in self.tasks:
            if task["id"] == task_id:
                task['description'] = new_description
                task['updatedAt'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.save_tasks()
                print(f"Task {task_id} updated successfully")
                return
        print(f"Task with ID {task_id} not found.")
    
    def delete_task(self, task_id):
        """Delete an existing task from the list and reorder IDs."""
        # Find and remove the task with the given ID
        task_to_remove = None
        for task in self.tasks:
            if task["id"] == task_id:
                task_to_remove = task
                break
        
        if task_to_remove:
            self.tasks.remove(task_to_remove)
            
            # Reorder the remaining tasks to have sequential IDs
            sorted_tasks = sorted(self.tasks, key=lambda x: x['id'])
            for new_id, task in enumerate(sorted_tasks, 1):
                task['id'] = new_id
            
            self.tasks = sorted_tasks
            self.save_tasks()
            print(f"Task {task_id} deleted successfully")
        else:
            print(f"Task with ID {task_id} not found.")
                
    def mark_task_status(self, task_id, status):
        """Mark a task's status."""
        for task in self.tasks:
            if task["id"] == task_id:
                task['status'] = status
                task['updatedAt'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.save_tasks()
                print(f"Task {task_id} marked as {status} successfully")
                return
        print(f"Task with ID {task_id} not found.")
        
    def list_tasks(self, filter_status=None):
        """List tasks, optionally filtered by status."""
        filtered_tasks = self.tasks
        
        if filter_status:
            filtered_tasks = [
                task for task in self.tasks
                    if task['status'] == filter_status
            ]
        
        if not filtered_tasks:
            print("No task found.")
            return
        
        print("ID | Description | Status | Created At | Updated At")
        print("-" * 70)
        for task in filtered_tasks:
            print(f"{task['id']} | {task['description']} | {task['status']} | {task['createdAt']} | {task['updatedAt']}")
    
def main():
    tracker = TaskTracker()
    
    if len(sys.argv) < 2:
        print("Usage: task-cli [add|update|delete|mark-in-progress|mark-done|list] [arguments]")
        sys.exit(1)
    
    command = sys.argv[1]
    
    try:
        if command == 'add' and len(sys.argv) > 2:
            tracker.add_task(sys.argv[2])
        elif command == 'update' and len(sys.argv) > 3:
            tracker.update_task(int(sys.argv[2]), sys.argv[3])
        elif command == 'delete' and len(sys.argv) > 2:
            tracker.delete_task(int(sys.argv[2]))
        elif command == 'mark-in-progress' and len(sys.argv) > 2:
            tracker.mark_task_status(int(sys.argv[2]), 'in-progress')
        elif command == 'mark-done' and len(sys.argv) > 2:
            tracker.mark_task_status(int(sys.argv[2]), 'done')
        elif command == 'list':
            if len(sys.argv) > 2:
                tracker.list_tasks(sys.argv[2])
            else:
                tracker.list_tasks()
        else:
            print("Invalid command. Use: task-cli [add|update|delete|mark-in-progress|mark-done|list] [arguments]")
            sys.exit(1)
    except ValueError:
        print("Invalid input. Task ID must be an integer.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()