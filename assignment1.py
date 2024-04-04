import os
import datetime

def display_menu():
    print("\nTODO List Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark Task as Completed")
    print("4. View Tasks")
    print("5. Exit")

def add_task(tasks):
    task_name = input("Enter task name: ")
    priority = input("Enter priority (high/medium/low): ")
    due_date_input = input("Enter due date (YYYY-MM-DD): ")

    try:
        due_date = datetime.datetime.strptime(due_date_input, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    tasks.append({"name": task_name, "priority": priority, "due_date": str(due_date), "completed": False})
    print("Task added successfully!")

def remove_task(tasks):
    task_index = int(input("Enter the index of the task to remove: ")) - 1
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        print("Task removed successfully!")
    else:
        print("Invalid task index!")

def mark_completed(tasks):
    task_index = int(input("Enter the index of the task to mark as completed: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task index!")

def view_tasks(tasks):
    print("\nTODO List:")
    for i, task in enumerate(tasks, 1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{i}. {task['name']} - Priority: {task['priority']}, Due Date: {task['due_date']}, Status: {status}")

def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(f"{task['name']},{task['priority']},{task['due_date']},{task['completed']}\n")

def load_tasks():
    tasks = []
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    tasks.append({
                        "name": parts[0],
                        "priority": parts[1],
                        "due_date": parts[2],
                        "completed": parts[3] == "True"
                    })
    return tasks

def main():
    tasks = load_tasks()
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            view_tasks(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Exiting...")
            
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()