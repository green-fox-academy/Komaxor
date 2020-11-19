import sys

def print_usage():
    print("$ todo\n\nCommand Line Todo application\n")
    print("=============================\n\nCommand line arguments\n")
    print("    -l   Lists all the tasks\n    -a   Adds a new task")
    print("    -r   Removes a task\n    -c   Completes a task")

def list_tasks():
    #open task file for reading
    try:
        with open("tasks.txt", 'r') as file:
            #read all lines
            lines = file.readlines()
            #no todos
            if len(lines) == 0:
                print("No todos for today! :)")
            #print lines
            else:
                i = 1
                for line in lines:
                    line = line.strip("\n")
                    print(str(i) + " - " + line)
                    i += 1
                file.close()
    #handle file missing exception
    except NameError:
        return "Name error"
    except FileNotFoundError:
        return "File is missing"
    except IOError:
        return "IO error"

def add_task(task):
    #open task file for writing
    try:
        with open("tasks.txt", 'a') as file:
        #append the new task to the end of the file
            file.write("\n" + task)
            file.close()
    #handle file missing exception
    except NameError:
        return "Name error"
    except FileNotFoundError:
        return "File is missing"
    except IOError:
        return "IO error"

#print(sys.argv)

arguments = ['-l', '-a']
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
    print("To add multiple words as one task, put them in quotation marks")
elif sys.argv[0] not in arguments:
    print("Unsupported argument")
    print_usage()
else:
    print("Unknown error")
