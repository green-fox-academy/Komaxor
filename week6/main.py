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

print(sys.argv)

#prints commands
if len(sys.argv) == 1:
    print_usage()
#list tasks
elif len(sys.argv) == 2 and sys.argv[1] == "-l":
    list_tasks()
