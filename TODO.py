tasks = []

def add_task():
    task_name = input("enter your task:")
    due_date = input("enter due date:")
    tasks.append({"name":task_name, "due_date": due_date, "completed": False})
   
    
def view_task():
    print("To-Do List:")
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Not Done"
        print(f"{i}. {task['name']} - Due: {task['due_date']} - Status: {status}")

def mark_comp():
    view_task()
    task_index = int(input("enter the index of completed task:")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        print("Task marked as completed")
    else:
        print("invalid task index!") 
def del_task():
    view_task()
    task_index = int(input("enter the index of the task to delete:")) - 1
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        print("your task deleted successfully")
    else :
        print("invalid task index!")

while True:
    print("\nMenu")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark_completed")
    print("4. Delete Task")
    print("5. Exit")
    
    choice = input("enter your choice: ")
    
    if choice == "1":
        add_task()
        
    elif choice == "2":
        view_task()
        
    elif choice == "3":
        mark_comp()
        
    elif choice == "4":
        del_task()
        
    elif choice == "5":
        print("Exiting the app.")
        break
    
    else:
        print("please enter valid choice")
    
    