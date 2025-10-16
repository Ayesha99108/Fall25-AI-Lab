def task(): 
    tasks = []
    print("This is my To Do List")
    total_tasks = int(input("Tasks to be added:"))

    for i in range (1, total_tasks+1):
        task_name = input(f"Enter the task {i}:")
        tasks.append(task_name)
    print("tasks are :",tasks)
    
    while True :
        opt = int(input("enter 1 to Add task: \n enter 2 to Delete task: \n enter 3 to Update tasks:\n enter 4 to View task:\n enter 5 to Mark task as Done:\n enter 6 to Prioritize task:\n enter 7 to Exit task"))

       
        if opt == 1 :
            add = input("Enter the task to be added:")
            tasks.append(add)
            print(f" Task {add} has been added")
        
        elif opt == 2:
            delete = input("Enter the task to be deleted:")
            if delete in tasks :
                ind = tasks.index(delete)
                del tasks[ind]
                print(f" task {delete} has been deleted")
        elif opt == 3:
            update = input("Enter the task to be updated:")
            if update in tasks :
                up = input("Enter new task:")
                ind = tasks.index(update)
                tasks[ind] = up
                print(f" Updated task {up}")
        elif opt == 4 :
            print(f" My total tasks are {tasks}")
       
      
        elif opt == 5:
            done = input("Enter the task to mark as done: ")
            if done in tasks:
               ind = tasks.index(done)
               tasks[ind] = done + " (Done)"
               print(f"Task '{done}' marked as done.")
   

        elif opt == 6:
            print("Enter the task you want to prioritize:")
            for level in ["High", "Medium", "Low"]:
                print(f"{level} Priority:")
                for t, p in zip(tasks, Prioritize):
                    if p.lower() == level.lower():
                        print(f" - {t}")
        
        elif opt == 7:
            print("Exiting the program")
            break

        else:
            print("Invalid input")
task()