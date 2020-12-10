import sys

def main(args):
    '''
    Calls `greet` function with command-line argument, or value
    obtained from user input.
    '''

    if len(sys.argv) > 1:
        subject = args[1]
    else:
        subject = input("Who to greet?: ")

    greet(subject)

    return 0


def greet (who, salutation='Hello'):
    '''
    Writes a greeting to standard output. If `None` or and empty
    string is passed, will use `World`.
    '''
    if not who or who is None:
        who = 'World'

    print(f'{salutation}, {who}!')


if __name__ == '__main__':
    sys.exit(main(sys.argv))