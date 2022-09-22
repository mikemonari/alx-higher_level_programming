#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    x = 1
    if (len(sys.argv) - 1) == 1 :
        print("{:d} argument:".format(len(sys.argv) - 1))
        print("{:d}: {:s}".format(len(sys.argv) - 1, str(sys.argv[x])))
    elif(len(sys.argv) - 1) > 1:
        print("{:d} arguments:".format(len(sys.argv) - 1))
        for arg in range(len(sys.argv)):
            while (x < len(sys.argv)):
                print("{}: {}".format(x, sys.argv[x]))
                x = x + 1
