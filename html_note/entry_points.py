from sys import argv
from . import generate
from . import help

def main():
    try:
        user_cmd = argv[1]
        if user_cmd == "generate":
            generate.main(argv[2])
        elif user_cmd == "help":
            help.main()
        else:
            print("Please supply a command - e.g help")
            RuntimeError("Please supply a command - e.g help")
    except IndexError:
        print("Please supply a command - e.g help")
        RuntimeError("Please supply a command - e.g help")
    return None
