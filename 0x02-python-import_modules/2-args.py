#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if (len(sys.argv) - 1) == 1 :
        print("{:d} argument:".format(len(sys.argv) - 1))
        print("{:d}: {:s}".format(len(sys.argv) - 1, str(sys.argv[1])))
    elif(len(sys.argv) - 1) > 1:
        print("{:d} arguments:".format(len(sys.argv) - 1))
        for i, arg in enumerate(sys.argv, start=1):
            print("{}: {}".format(i, arg))
