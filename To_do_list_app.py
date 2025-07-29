tasks = []

def addTask():
    task = input('Please enter a task: \n')
    tasks.append({"description": task, "completed": False})
    print(f"Task '{task}' added to the list.\n")


def listTasks():
    if not tasks:
        print("There are no tasks currently.\n")
    else:
        print("Here are the current tasks: \n")
        for index, task in enumerate(tasks):
            status = "Completed task: " if task["completed"] else "Incomplete task: "
            print(f'{index + 1}. {status} {task["description"]}')
        print()


def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the number of the task to delete: "))
        if 1 <= taskToDelete <= len(tasks):
            removed = tasks.pop(taskToDelete - 1)
            print(f'Task "{removed["description"]}" has been removed.\n')
        else:
            print(f"Task number {taskToDelete} was not found!\n")
    except:
        print("Invalid input. Please enter a number.\n")


def markTaskCompleted():
    listTasks()
    try:
        taskToMark = int(input("Enter the number of the task to mark as completed: "))
        if 1 <= taskToMark <= len(tasks):
            tasks[taskToMark - 1]["completed"] = True
            print(f'Task "{tasks[taskToMark - 1]["description"]}" marked as completed.\n')
        else:
            print("Invalid task number.\n")
    except:
        print("Invalid input. Please enter a number.\n")


if __name__ == "__main__":

    print("\nWelcome to the To Do List App")
    print('*' * 80)

    while True:
        print("What would you like to do?")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Remove a task")
        print("4. Mark a task as completed")
        print("5. Exit")
        print('-' * 80)

        choice = input("Enter your choice: ")

        if choice == "1":
            addTask()
        elif choice == "2":
            listTasks()
        elif choice == "3":
            deleteTask()
        elif choice == "4":
            markTaskCompleted()
        elif choice == "5":
            print("Exiting the app...")
            break
        else:
            print("Invalid choice, try again!\n")
