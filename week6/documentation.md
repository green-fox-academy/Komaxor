1. Have the repository cloned to your device.
2. Open the terminal and navigate inside the directory/repository.
3. Type "python3 main.py" then the argument(s) to interact with the todo app.

The arguments are the following:

-l
Lists all the tasks
It has no further arguments.
How to use: python3 main.py -l

-a
Adds a new task
It has one additional argument, which is the task itself that needs to be added
How to use: python3 main.py -a "task here"
If the task to be added is just 1 word, the quotation marks are not required.

-r
Removes a task
It has one additional argument, the index of the task that needs to be removed
How to use: python3 main.py -r 1

-c
Checks a task
It has one additional argument, the index of the task that needs to be checked
How to use: python3 main.py -c 1

-m
Modifies a task
It has two additional arguments, the first is the index of the task that needs to be modified, the second is the new text of the task
How to use: python3 main.py -m 1 "modified task here"

If the user input is incorrect, the app will display informative error messages.