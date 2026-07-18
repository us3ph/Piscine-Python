import sys

if len(sys.argv) > 2:
    print("AssertionError: more than one argument is provided")
    exit(1)

if sys.argv[1].isdigit() != True:
    print("AssertionError: argument is not an integer")
    exit(1)

if int(sys.argv[1]) % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
