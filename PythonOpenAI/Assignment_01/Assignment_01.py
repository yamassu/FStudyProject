#• Add new tasks 
#• View all tasks 
#• Mark tasks as completed 
#• Delete tasks 
tasks = [] 
def add_task(description): 
task_id = tasks[-1]["id"] + 1 if tasks else 1 
task = {"id": task_id, "description": description, "completed": False} 
tasks.append(task) 
print(f"Task '{description}' added with ID {task_id}.") 
def view_tasks(): 
if not tasks: 
print("No tasks available.") 
return 
for task in tasks: 
    status = "Done" if task["completed"] else "Pending" 
    print(f"{task['id']}: {task['description']} [{status}]") 

def mark_completed(task_id): 
    for task in tasks: 
    if task["id"] == task_id: 
    task["completed"] = True 
    print(f"Task ID {task_id} marked as completed.") 
return 

print(f"No task found with ID {task_id}.") 
def delete_task(task_id): 
    global tasks 
    tasks = [task for task in tasks if task["id"] != task_id] 
    print(f"Task ID {task_id} deleted if it existed.") 
  
def main(commands): 
    for command in commands: 
        choice = command[0] 
        if choice == "add": 
            if len(command) > 1: 
                desc = command[1] 
                add_task(desc) 
            else: 
                print("Add command requires a description.") 
        elif choice == "view": 
            view_tasks() 
        elif choice == "complete": 
            if len(command) > 1: 
                try: 
                    task_id = int(command[1]) 
                    mark_completed(task_id) 
                except ValueError: 
                    print("Invalid task ID.") 
            else: 
                print("Complete command requires a task ID.") 
        elif choice == "delete": 
            if len(command) > 1: 
                try: 
                    task_id = int(command[1]) 
                    delete_task(task_id) 
                except ValueError: 
                    print("Invalid task ID.") 
            else: 
                print("Delete command requires a task ID.") 
        elif choice == "exit": 
            print("Exiting Task Manager. Goodbye!") 
            break 
        else: 
            print(f"Invalid command: {choice}") 
  
if __name__ == "__main__": 
    # Example of automated input 
    commands_to_execute = [ 
        ("add", "Buy groceries"), 
        ("add", "Walk the dog"), 
        ("view",), 
        ("complete", "1"), 
        ("view",), 
        ("delete", "2"), 
        ("view",), 
("exit",) 
] 
main(commands_to_execute)
input("Nhấn Enter để tiếp tục...")