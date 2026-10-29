''' This is the first project of to do application build on the python tech stack.'''
tasks=[]
completed_task=set() 

#add a task
def add_task():
    task=input("Please enter the new task here : ")
    tasks.append(task)
    print(f"{task} > added successfully to the task list\n")

#view the task 
def view_task():
    if not tasks:
        print("No task is available to display")
    print("\n     TO DO LIST       ")
    for idx,task in enumerate(tasks,start=1):
        status="✅Completed" if task in completed_task else "Pending"
        print(f"{idx}. {task} - {status}")
# mark the task as completed
def mark_completed(task_number):
    "Mark a task as completed uding its name "
    if 1<=task_number<=len(tasks):
        task_item=tasks[task_number-1]
        completed_task.add(task_item)
        print(f"Task >> {task_item} << marked as completed.\n")
    else: 
        print("Invalid task number.\n")

#delete a task
def delete_task(task_number):
    if 1<=task_number <=len(tasks):
        task_item=tasks.pop(task_number-1)
        completed_task.discard(task_item)
        print(f"Task >> {task_item} << delete successfully.\n")
    else: 
        print("Invalid task number.\n")
print("""==== TO DO LIST APP===
      1.ADD TASK
      2.VIEW TASK
      3.Mark Task
      4.delete Task
      5.exit
      """)
while True:
    choice=input("Enter your choice(1-5):")
    if choice=="1":
        add_task()
    elif choice=="2":
        view_task()
    elif choice=="3":
        task_no=int(input("Enter the task no. to mark comleted -> "))
        mark_completed(task_no)
    elif choice=="4":
        task_no=int(input("Enter the task no. to mark delete -> "))
        delete_task(task_no)
    elif choice=="5":
        print("BYEEE")
        break
    else:
        print("Invalid choice,Please try again.\n")
