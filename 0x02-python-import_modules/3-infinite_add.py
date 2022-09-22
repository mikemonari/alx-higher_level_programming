#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    x = 1
    lis = []
    for arg in range(len(sys.argv)):
        while (x < len(sys.argv)):
            lis.append(int(sys.argv[x]))
            x = x + 1
    print("{}".format(sum(lis)))
