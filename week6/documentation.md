Background:
The project was created using VS Code, git and Python using macOS.

File structure:
The project consists of 2 files outside this documentation: main.py and .tasks.txt.
main.py was written in python and is meant to be used with Python 3.x.
.tasks.txt stores the tasks. It is hidden to prevent unwanted modifications by the user.

Required to launch:
1. Have the repository cloned to your device.
2. Have Pthon 3.x installed on your device.
3. Open the terminal and navigate inside the directory.
4. Type "python3 main.py" then the argument(s) to interact with the todo app.


How to use:
If you run without arguments, it will print the usage.

The arguments are the following:

-l
Lists all the tasks.
It has no further arguments.
Example: python3 main.py -l

-a
Adds a new task
It has one additional argument, which is the task itself that needs to be added.
Example: python3 main.py -a "task here"
If the task to be added is just 1 word, the quotation marks are not required.

-r
Removes a task
It has one additional argument, the index of the task that needs to be removed.
Example: python3 main.py -r 1

-c
Checks a task
It has one additional argument, the index of the task that needs to be checked.
Example python3 main.py -c 1

-m
Modifies a task
It has two additional arguments, the first is the index of the task that needs to be modified, the second is the new text of the task.
Example: python3 main.py -m 1 "modified task here"

If the user input is incorrect, the app will display informative error messages.

Code structure:
The core of the app is an if-elif structure. The app checks for a certain scenario, then for another until all possible scenarios are checked. These are determined by the number of arguments and the content of those arguments.

Unsupported arguments are not accepted.

If more arguments are provided than necessay, the app lets the user know about that.
In case of listing, the app executes the list_tasks() function, but other arguments are ignored.

If less arguments are provided than necessary when modifying, the app tells the user that both the index and the text of the new task are necessary.

In case of removing, checking or modifying, only the existing indexes are acceptable arguments.

The NameError, FileNotFoundError and the IOError are handled when dealing with the file .tasks.txt file.

All lines in the .tasks.txt should start with "[ ]" or "[x]". If for some reason the line would not start like that, when checking or modifying, the app stops, lets the user know that the file is corrupted and how the incorrectly formatted line should be deleted.

The print_usage() function is activated if the app is launched without arguments. It prints the header then lists the possible arguments and what they do.

The get_tasks() function creates a list of the existing tasks stored in the .tasks.txt file, while the set_tasks(tasks) function writes the list of tasks in the .tasks.txt file.

The list_tasks() function lists the tasks in a numbered order, and shows which are checked and which are not.
The add_task(task) function adds the argument as an unchecked task to the .tasks.txt file
The remove_task() function removes a task with the given index from the tasks.txt file.
The check_task() checks if it is unchecked, or unchecks if it is checked the task with the given index.
The modify_task() changes the task with the given index to the given text.
