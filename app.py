
tasks = []

def addTask():
    task = input('Please enter a task: \n')
    tasks.append(task)
    print(f"Task {task} added to the list")


def listTasks():
    if not tasks:
        print("There are no tasks currently.")

    else:
        print("Here are the current tasks: \n")

        for index, task in enumerate(tasks):
            print(f'Task {index + 1}. {task}')


def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the number of task to delete: "))
        if taskToDelete >= 0 and taskToDelete > len(tasks):
            tasks.pop(taskToDelete)
            print(f'Task {taskToDelete} has been removed.')

        else:
            print(f"Task number {taskToDelete} was not found!")

    except:
        print("Invalid Input")

if __name__ == "__main__":

    ## Create a Loop to run the app

    print("\nWelcome to the To Do List App")

    print('*' * 80)
    while True:
        print("What would you like to do?")

        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Remove a task")
        print("4. Exit")

        print('-' * 80)

        choice = input("Enter your choice: ")

        if choice == "1":
            addTask()

        elif choice == "2":
            listTasks()

        elif choice == "3":
            deleteTask()

        elif choice == "4":
            print("Exiting the app...")
            break

        else:
            print("Invalid choice, try again!")
