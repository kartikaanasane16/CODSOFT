import json
import os

FILENAME = "tasks.json"

# -----------------------------
# Load and Save Functions
# -----------------------------
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []  # if file is empty or invalid
    return []

def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=4)

# -----------------------------
# Display Function
# -----------------------------
def show_tasks(tasks):
    print("\n------ TO-DO LIST ------")
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, start=1):
            status = "✅" if task["done"] else "❌"
            print(f"{i}. {task['task']} [{status}]")

# -----------------------------
# Main Program
# -----------------------------
def main():
    tasks = load_tasks()   # ✅ tasks is defined here

    while True:
        print("\nOptions: ")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter new task: ")
            tasks.append({"task": task_name, "done": False})
            save_tasks(tasks)
            print("Task added!")

        elif choice == "2":
            show_tasks(tasks)

        elif choice == "3":
            show_tasks(tasks)
            if tasks:
                num = int(input("Enter task number to mark done: "))
                if 1 <= num <= len(tasks):
                    tasks[num - 1]["done"] = True
                    save_tasks(tasks)
                    print("Task marked as done!")
                else:
                    print("Invalid number!")

        elif choice == "4":
            show_tasks(tasks)
            if tasks:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    tasks.pop(num - 1)
                    save_tasks(tasks)
                    print("Task deleted!")
                else:
                    print("Invalid number!")

        elif choice == "5":
            print("Goodbye 👋")
            break

        else:
            print("Invalid option. Try again.")

# -----------------------------
# Entry Point
# -----------------------------
if __name__ == "__main__":
    main()

