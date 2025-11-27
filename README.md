📝 To-Do List Application (Python)

This is a simple command-line To-Do List application written in Python.
It allows users to add tasks, view tasks, mark tasks as completed, and delete tasks.
All tasks are stored in a tasks.json file so data is saved even after closing the program.

🚀 Features

Add new tasks

View all tasks

Mark tasks as completed

Delete tasks

Persistent storage using JSON

Simple and clean menu-driven interface

📁 Project Structure
To do list.py
tasks.json  (auto-created)

▶️ How to Run

Make sure Python is installed.

Save the script as To do list.py.

Open terminal/cmd in the folder where the file is stored.

Run:

python "To do list.py"

📌 How It Works
1️⃣ Add Task

User enters a task, and it gets stored as:

{"task": "Your task", "done": false}

2️⃣ View Tasks

Displays all tasks with status:

✅ → Completed

❌ → Not completed

3️⃣ Mark Task as Done

User selects the task number to mark it as completed.

4️⃣ Delete Task

Removes a task permanently from the list.

🛠️ Technologies Used

Python

JSON file handling

Basic command-line interface

📦 JSON Storage Example
[
    {
        "task": "Study Python",
        "done": false
    },
    {
        "task": "Complete project",
        "done": true
    }
]