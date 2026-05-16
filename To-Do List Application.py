# To-Do List Application in Python

import json
import os

FILE_NAME = "tasks.json"

# Load tasks from JSON file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks to JSON file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(tasks):
    task_name = input("Enter task: ")

    task = {
        "task": task_name,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print("✅ Task added successfully!")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("📂 No tasks available.")
        return

    print("\n📋 To-Do List:")
    
    for index, task in enumerate(tasks, start=1):
        status = "✔ Done" if task["completed"] else "❌ Not Done"
        print(f"{index}. {task['task']} - {status}")

# Mark task as completed
def mark_completed(tasks):
    view_tasks(tasks)

    try:
        task_num = int(input("Enter task number to mark as completed: "))

        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            save_tasks(tasks)

            print("✅ Task marked as completed!")

        else:
            print("❌ Invalid task number.")

    except ValueError:
        print("❌ Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)

    try:
        task_num = int(input("Enter task number to delete: "))

        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)

            print(f"🗑 Task '{removed['task']}' deleted successfully!")

        else:
            print("❌ Task does not exist.")

    except ValueError:
        print("❌ Please enter a valid number.")

# Main Program
def main():
    tasks = load_tasks()

    while True:
        print("\n====== TO-DO LIST MENU ======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            mark_completed(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("👋 Exiting To-Do List Application...")
            break

        else:
            print("❌ Invalid choice. Please try again.")

# Run program
main()