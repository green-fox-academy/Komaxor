import sys

def print_usage():
    print("$ todo\n\nCommand Line Todo application\n")
    print("=============================\n\nCommand line arguments\n")
    print("    -l   Lists all the tasks\n    -a   Adds a new task")
    print("    -r   Removes an task\n    -c   Completes an task")

def list_tasks():
    #empty list
    if len("tasks.txt") == 0:
        print("No todos for today! :)")
    else:
        #open task file for reading
        try:
            with open("tasks.txt", 'r') as file:
                #read all lines and print them
                i = 1
                for line in file:
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
            file.write("\n[ ] " + task)
            file.close()
    #handle file missing exception
    except NameError:
        return "Name error"
    except FileNotFoundError:
        return "File is missing"
    except IOError:
        return "IO error"

def remove_task():
    #open task file for reading
    try:
        with open("tasks.txt", 'r') as file:
            #read all lines
            line_count = 0
            lines = file.readlines()
            for _ in lines:
                line_count += 1
            file.close()
    #handle file missing exception
    except NameError:
        return "Name error"
    except FileNotFoundError:
        return "File is missing"
    except IOError:
        return "IO error"
    #error handling
    if int(sys.argv[2]) > line_count:
        print("Unable to remove: index is out of bound")
    else:
        #open task file for writing
        #try:
            with open("tasks.txt", 'w') as file:
            #remove the task with the given index from file
            #TODO if first line is empty, it crashes
            #TODO if I remove last item, empty line remians
                num = 1
                for line in lines:
                    if line[num] != line[int(sys.argv[2])]:
                        file.write(line)
                    num += 1
                file.close()
        #handle file missing exception
        #except NameError:
            #return "Name error"
        #except FileNotFoundError:
            #return "File is missing"
        #except IOError:
            #return "IO error"

def check_task():
    #open task file for reading
    try:
        with open("tasks.txt", 'r') as file:
            #read all lines
            line_count = 0
            lines = file.readlines()
            for _ in lines:
                line_count += 1
            file.close()
    #handle file missing exception
    except NameError:
        return "Name error"
    except FileNotFoundError:
        return "File is missing"
    except IOError:
        return "IO error"
    #error handling
    if int(sys.argv[2]) > line_count:
        print("Unable to check: index is out of bound")
    else:
        #open task file for writing
        try:
            with open("tasks.txt", 'w') as file:
            #chesck the task with the given index from file
                num = 1
                for line in lines:
                    if line[num] != line[int(sys.argv[2])]:
                            file.write(line)
                    else:
                        if line[1] == "x":
                            line = line.replace("x", " ", 1) #file.write("[ ]" + line[2:])
                            file.write(line)
                        elif line[1] == " ":
                            line = line.replace(" ", "x", 1) #file.write("[ ]" + line[2:])
                            file.write(line)
                        else:
                            print("Unexpectedd error when checking the file")
                    num += 1
                file.close()
        #handle file missing exception
        except NameError:
            return "Name error"
        except FileNotFoundError:
            return "File is missing"
        except IOError:
            return "IO error"

print(sys.argv)
arg = ['-l', '-a', '-r', '-c']
#print commands
if len(sys.argv) == 1:
    print_usage()
#list tasks
elif len(sys.argv) == 2 and sys.argv[1] == "-l":
    list_tasks()
#add new task
elif len(sys.argv) == 3 and sys.argv[1] == "-a":
    add_task(sys.argv[2])
#add new task error handling
elif len(sys.argv) == 2 and sys.argv[1] == "-a":
    print("Unable to add: no task provided")
#remove error not number
elif (len(sys.argv) == 3 and sys.argv[1] == "-r" and
        not sys.argv[2].isdigit()):
    print("Unable to remove: index is not a number")
#remove task
elif len(sys.argv) == 3 and sys.argv[1] == "-r":
    remove_task()
#remove task no index
elif len(sys.argv) == 2 and sys.argv[1] == "-r":
    print("Unable to remove: no index provided")
#check error not number
elif (len(sys.argv) == 3 and sys.argv[1] == "-c" and
        not sys.argv[2].isdigit()):
    print("Unable to check: index is not a number")
#check task
elif len(sys.argv) == 3 and sys.argv[1] == "-c":
    check_task()
#check task no index
elif len(sys.argv) == 2 and sys.argv[1] == "-c":
    print("Unable to check: no index provided")
#unsupported argument eror handling
elif sys.argv[0] not in arg:
    print("Unsupported argument")
    print_usage()
    #error: if I add multiple elements, this gets triggered
else:
    print("Unknown error")

#TODO ask why at least 2 tasks?