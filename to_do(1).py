# Define the tasks list to store our to-dos
tasks = []

# Function to display all tasks
def display_tasks():
    if not tasks:
        print("Your To-Do list is empty.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

# Function to add a new task
def add_task(task):
    tasks.append(task)
    print(f"Added '{task}' to your To-Do list.")

# Function to remove a task by its number
def remove_task(task_number):
    try:
        removed_task = tasks.pop(task_number - 1)
        print(f"Removed '{removed_task}' from your To-Do list.")
    except IndexError:
        print("Invalid task number.")

def main():
    while True:
        # Display the menu options
        print("\n--- To-Do List App ---")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        
        # Get user input
        choice = input("Please choose an option: ")

        # Handle the user's choice
        if choice == '1':
            display_tasks()
        elif choice == '2':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '3':
            task_number = input("Enter the task number to remove: ")
            if task_number.isdigit():
                remove_task(int(task_number))
            else:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 4.")

# Run the main function to start the app
if __name__ == "__main__":
    main()