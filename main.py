def add_task(tasks, name, description):
    task = {"name": name, "status": "Incomplete"}
    tasks.append(task)
    print(f"Task '{name}' added successfully!")

def list_tasks(tasks, show_all=True):
    if tasks:
        print("To-Do List:")
        for index, task in enumerate(tasks, start=1):
            if show_all or task['status'] == 'Incomplete':
                print(f"{index}. {task['name']}  - {task['status']}")
    else:
        print("To-Do List is empty.")

def mark_task_complete(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]["status"] = "Complete"
        print(f"Task '{tasks[task_index - 1]['name']}' marked as complete.")
    else:
        print("Invalid task index.")

def clear_tasks(tasks):
    confirmation = input("Are you sure you want to clear the entire to-do list? (yes/no): ").lower()
    if confirmation == "yes":
        tasks.clear()
        print("To-Do List cleared successfully!")
    else:
        print("Operation canceled.")

def edit_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        task = tasks[task_index - 1]
        print(f"Editing task '{task['name']}'. Enter new details:")
        name = input("Enter task name: ")
        task["name"] = name
        print(f"Task '{name}' edited successfully.")
    else:
        print("Invalid task index.")

tasks = []

while True:
    print("\nTo-Do List Manager\n")
    print("1. Add a new task")
    print("2. List all tasks")
    print("3. Mark a task as completed")
    print("4. Clear the entire to-do list")
    print("5. Edit a task")
    print("6. List incomplete tasks")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        name = input("Enter task name: ")
        description = input("Enter task description: ")
        add_task(tasks, name, description)
    elif choice == "2":
        list_tasks(tasks)
    elif choice == "3":
        task_index = int(input("Enter the index of the task to mark as complete: "))
        mark_task_complete(tasks, task_index)
    elif choice == "4":
        clear_tasks(tasks)
    elif choice == "5":
        task_index = int(input("Enter the index of the task to edit: "))
        edit_task(tasks, task_index)
    elif choice == "6":
        list_tasks(tasks, show_all=False)
    elif choice == "7":
        print("Exiting To-Do List Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
