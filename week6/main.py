import sys

def print_usage():
    #print header
    print("$ todo\n\nCommand Line Todo application\n")
    print("=============================\n\nCommand line arguments:")
    #print arguments
    print("\t-l\tLists all the tasks")
    print("\t-a\tAdds a new task")
    print("\t-r\tRemoves a task")
    print("\t-c\tCompletes a task")
    print("\t-m\tModifies a task")

def get_tasks():
    #open task file for reading
    try:
        with open(".tasks.txt", 'r') as file:
            #read all lines
            lines = file.readlines()
            #create list without linebreaks
            tasks = []
            for i in range(len(lines)):
                tasks.append(lines[i].replace("\n", ""))
                tasks = list(filter(None, tasks))
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
        with open(".tasks.txt", 'w') as file:
            #enter the tasks in the file
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
    #get to do list
    tasks = get_tasks()
    #check for empty to do list
    if len(tasks) == 0:
        print("No todos for today! :)")
    #print tasks with numbers attached
    else:
        current_task = 1
        for task in tasks:
            print(str(current_task) + " - " + task)
            current_task += 1

def add_task(task):
    #get to do list
    tasks = get_tasks()
    #add new unchecked task
    tasks.append("[ ] " + task)
    #enter the tasks in the file
    set_tasks(tasks)

def remove_task():
    #get to do list
    tasks = get_tasks()
    #index out of range error
    if int(sys.argv[2]) > len(tasks):
        print("Unable to remove: index is out of bound")
    else:
        #remove task from list
        tasks.remove(tasks[int(sys.argv[2]) - 1])
    #enter the tasks in the file
    set_tasks(tasks)        #remove the task with the given index from file

def check_task():
    #get to do list
    tasks = get_tasks()
    #index out of range error
    if int(sys.argv[2]) > len(tasks):
        print("Unable to check: index is out of bound")
    else:
        #check task
        checked_tasks = []
        checked_task = tasks[int(sys.argv[2]) - 1]
        if checked_task[:3] == "[x]":
            checked_task = checked_task.replace("[x]", "[ ]", 1)
        elif checked_task[:3] == "[ ]":
            checked_task = checked_task.replace("[ ]", "[x]", 1)
        else:
            #file content format is not appropriate
            print("Corrupted file. Remove the task with this index.")
            return
        for i in range(len(tasks)):
            if i != int(sys.argv[2]) - 1:
                checked_tasks.append(tasks[i])
            else:
                checked_tasks.append(checked_task)
        #enter the tasks in the file
        set_tasks(checked_tasks)

def modify_task():
    #get to do list
    tasks = get_tasks()
    #index out of range error
    if int(sys.argv[2]) > len(tasks):
        print("Unable to modify: index is out of bound")
    else:
        #modify text of the task
        modified_tasks = []
        if tasks[int(sys.argv[2]) - 1][:3] == "[x]":
            modified_task = "[x] " + sys.argv[3]
        elif tasks[int(sys.argv[2]) - 1][:3] == "[ ]":
            modified_task = "[ ] " + sys.argv[3]
        else:
            #file content format is not appropriate
            print("Corrupted file. Remove the task with this index.")
            return
        for i in range(len(tasks)):
            if i != int(sys.argv[2]) - 1:
                modified_tasks.append(tasks[i])
            else:
                modified_tasks.append(modified_task)
        #enter the tasks in the file
        set_tasks(modified_tasks)

arguments = ['-l', '-a', 'r', 'c', 'm']
#print commands
if len(sys.argv) == 1:
    print_usage()
#list tasks
elif len(sys.argv) == 2 and sys.argv[1] == "-l":
    list_tasks()
#list tasks too many arguments error
elif len(sys.argv) > 2 and sys.argv[1] == "-l":
    print("-l does not have any arguments.")
#add new task
elif len(sys.argv) == 3 and sys.argv[1] == "-a":
    add_task(sys.argv[2])
#add new task no task error
elif len(sys.argv) == 2 and sys.argv[1] == "-a":
    print("Unable to add: no task provided.")
#add too many arguments error
elif len(sys.argv) > 3 and sys.argv[1] == "-a":
    print("You can only add one task at a time.")
    print("To add multiple words as one task, put them in quotation marks.")
#remove index not number error
elif len(sys.argv) == 3 and sys.argv[1] == "-r" and not sys.argv[2].isdigit():
    print("Unable to remove: index is not a number.")
#remove index zero error
elif len(sys.argv) == 3 and sys.argv[1] == "-r" and int(sys.argv[2]) == 0:
    print("Unable to remove: index cannot be 0.")
#remove task
elif len(sys.argv) == 3 and sys.argv[1] == "-r":
    remove_task()
#remove task no index error
elif len(sys.argv) == 2 and sys.argv[1] == "-r":
    print("Unable to remove: no index provided.")
#remove too many arguments error
elif len(sys.argv) > 3 and sys.argv[1] == "-r":
    print("You can only remove one task at a time.")
#check index not number error
elif len(sys.argv) == 3 and sys.argv[1] == "-c" and not sys.argv[2].isdigit():
    print("Unable to check: index is not a number.")
#check index zero error
elif len(sys.argv) == 3 and sys.argv[1] == "-c" and int(sys.argv[2]) == 0:
    print("Unable to check: index cannot be 0.")
#check task
elif len(sys.argv) == 3 and sys.argv[1] == "-c":
    check_task()
#check task no index error
elif len(sys.argv) == 2 and sys.argv[1] == "-c":
    print("Unable to check: no index provided.")
#check too many arguments error
elif len(sys.argv) > 3 and sys.argv[1] == "-c":
    print("You can only check one task at a time.")
#modify index not number error
elif len(sys.argv) == 4 and sys.argv[1] == "-m" and not sys.argv[2].isdigit():
    print("Unable to modify: index is not a number.")
#modify index zero error
elif len(sys.argv) == 4 and sys.argv[1] == "-m" and int(sys.argv[2]) == 0:
    print("Unable to modify: index cannot be 0.")
#modify task
elif len(sys.argv) == 4 and sys.argv[1] == "-m":
    modify_task()
#modify task no index
elif len(sys.argv) == 2 and sys.argv[1] == "-m":
    print("Unable to modify: no index provided.")
#modify one argument missing
elif len(sys.argv) == 3 and sys.argv[1] == "-m":
    print("The index or the task is missing.")
#modify too many arguments error
elif len(sys.argv) > 4 and sys.argv[1] == "-m":
    print("Too many arguments given. Enter the index then the task")
    print("To enter multiple words as one task, put them in quotation marks.")
#unsupported argument
elif sys.argv[0] not in arguments:
    print("Unsupported argument")
    print_usage()
#unknown error
else:
    print("Unknown error")
