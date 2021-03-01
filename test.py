import sys

class hello():
    def __init__(self):
        print('Hello World')

    def input(self, args):
        print('Hello,'+str(args))

if __name__ == "__main__":
    a = hello()
    a.input(sys.argv[1])
