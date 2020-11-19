import sys

def print_usage():
    print("$ todo\n\nCommand Line Todo application\n")
    print("=============================\n\nCommand line arguments\n")
    print("    -l   Lists all the tasks\n    -a   Adds a new task")
    print("    -r   Removes a task\n    -c   Completes a task")

print(sys.argv)

if len(sys.argv) == 1:
    print_usage()
