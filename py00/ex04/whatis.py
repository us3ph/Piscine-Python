import sys


def main():
    # check if the number of arguments is correct
    if len(sys.argv) < 2:
        return
    # check if the argument is an integer
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")
   # check if the argument is an integer
    try:
        num = int(sys.argv[1])
    except ValueError:
      # if the argument is not an integer, raise a ValueError
      # AssertionError is a built in expection in python that is raised when an assertion statement fails
        raise AssertionError("argument is not an integer")
    if num % 2 == 0:
        print("even")
    else:
        print("odd")

if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")



