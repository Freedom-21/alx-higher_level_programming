#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    totargs = len(sys.argv)
    sum = 0
    if totargs == 1:
        print("0")
    if totargs > 1:
        for i in range(1, totargs):
            sum += int(sys.argv[i])
        print(sum)
