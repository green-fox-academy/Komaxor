import sys

def print_usage():
    print("$ todo\n\nCommand Line Todo application\n")
    print("=============================\n\nCommand line arguments\n")
    print("    -l   Lists all the tasks\n    -a   Adds a new task")
    print("    -r   Removes a task\n    -c   Completes a task")

def get_tasks():
    #open task file for reading
    try:
        with open("tasks.txt", 'r') as file:
            #read all lines
            lines = file.readlines()
            #remove linebreaks
            tasks = []
            for i in range(len(lines)):
                tasks.append(lines[i].replace("\n", ""))
                tasks = list(filter(None, tasks))
            print(tasks)
            file.close()
            return tasks
    #handle exceptions
    except NameError:
        return "Name error"
    except FileNotFoundError:
        return "File is missing"
    except IOError:
        return "IO error"

def set_tasks(tasks):
    #open task file for writing
    try:
        with open("tasks.txt", 'w') as file:
            #write tasks in file
            for task in tasks:
                file.write(task + "\n")
            file.close()
    #handle exceptions
    except NameError:
        return "Name error"
    except FileNotFoundError:
        return "File is missing"
    except IOError:
        return "IO error"

def list_tasks():
    tasks = get_tasks()
    if len(tasks) == 0:
        print("No todos for today! :)")
    #print tasks with numbers attached
    else:
        current_task = 1
        for task in tasks:
            print(str(current_task) + " - " + task)
            current_task += 1

def add_task(task):
    #get tasks
    tasks = get_tasks()
    #add new task
    tasks.append(task)
    set_tasks(tasks)

def remove_task():
    tasks = get_tasks()        #index out of range error
    if int(sys.argv[2]) > len(tasks):
        print("Unable to remove: index is out of bound")
    else:
        tasks.remove(tasks[int(sys.argv[2]) - 1])
    set_tasks(tasks)        #remove the task with the given index from file

def check_task():
    tasks = get_tasks()        #index out of range error
    if int(sys.argv[2]) > len(tasks):
        print("Unable to check: index is out of bound")
    else:
        set_tasks(tasks)

#print(sys.argv)

arguments = ['-l', '-a', 'r', 'c']
#prints commands
if len(sys.argv) == 1:
    print_usage()
#list tasks
elif len(sys.argv) == 2 and sys.argv[1] == "-l":
    list_tasks()
#list tasks more
elif len(sys.argv) > 2 and sys.argv[1] == "-l":
    print("-l does not have any extensions")
#add new task
elif len(sys.argv) == 3 and sys.argv[1] == "-a":
    add_task(sys.argv[2])
#add new task error handling
elif len(sys.argv) == 2 and sys.argv[1] == "-a":
    print("Unable to add: no task provided")
#add multiple tasks error
elif len(sys.argv) > 3 and sys.argv[1] == "-a":
    print("You can only add one task at a time.")
    print("To add multiple words as one task, put them in quotation marks.")
#remove task
elif (len(sys.argv) == 3 and sys.argv[1] == "-r" and
        sys.argv[2].isdigit()):
    remove_task()
#remove error not number
elif (len(sys.argv) == 3 and sys.argv[1] == "-r" and
        not sys.argv[2].isdigit()):
    print("Unable to remove: index is not a number")
#remove task no index
elif len(sys.argv) == 2 and sys.argv[1] == "-r":
    print("Unable to remove: no index provided")
#remove multiple
elif len(sys.argv) > 3 and sys.argv[1] == "-r":
    print("You can only remove 1 task at a time.")
#check task
elif (len(sys.argv) == 3 and sys.argv[1] == "-c" and
        sys.argv[2].isdigit()):
    check_task()
#check error not number
elif (len(sys.argv) == 3 and sys.argv[1] == "-c" and
        not sys.argv[2].isdigit()):
    print("Unable to check: index is not a number")
#check task no index
elif len(sys.argv) == 2 and sys.argv[1] == "-c":
    print("Unable to check: no index provided")
#remove multiple
elif len(sys.argv) > 3 and sys.argv[1] == "-c":
    print("You can only check 1 task at a time.")
#unsupported argument
elif sys.argv[0] not in arguments:
    print("Unsupported argument")
    print_usage()
#unknown error
else:
    print("Unknown error")
