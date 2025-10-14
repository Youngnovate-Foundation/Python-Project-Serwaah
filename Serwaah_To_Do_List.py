# Simple To-Do List Application
# Mini Project

tasks = []  # List to store tasks


def show_menu():
    print("\n--- TO-DO LIST APP ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")


while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append({"task": task, "done": False})
        print("Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, start=1):
                status = "completed" if t["done"] else "not completed"
                print(f"{i}. {t['task']} - {status}")

    elif choice == "3":
        if not tasks:
            print("No tasks to mark.")
        else:
            num = int(input("Enter task number to mark as done: "))
            if 1 <= num <= len(tasks):
                tasks[num - 1]["done"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number!")

    elif choice == "4":
        if not tasks:
            print("No tasks to delete.")
        else:
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                deleted = tasks.pop(num - 1)
                print(f"Deleted: {deleted['task']}")
            else:
                print("Invalid task number!")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 5.")
