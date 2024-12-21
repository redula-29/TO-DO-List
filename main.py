from task_manager import load_tasks, save_tasks
from menu import display_menu

def main():
    tasks = load_tasks()
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            print("\nYour Tasks:")
            if not tasks:
                print("No tasks found!")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
        
        elif choice == "2":
            new_task = input("Enter a new task: ")
            tasks.append(new_task)
            save_tasks(tasks)
            print(f"Task '{new_task}' added.")
        
        elif choice == "3":
            if not tasks:
                print("No tasks to mark as done!")
            else:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                task_num = int(input("Enter the task number to mark as done: "))
                if 1 <= task_num <= len(tasks):
                    completed_task = tasks.pop(task_num - 1)
                    save_tasks(tasks)
                    print(f"Task '{completed_task}' marked as done.")
                else:
                    print("Invalid task number!")
        
        elif choice == "4":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
