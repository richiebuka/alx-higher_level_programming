#!/usr/bin/python3
import sys
if __name__=="__main__":
    l = len(sys.argv)
    answer = 0
    for i in range(1, l):
        answer += int(sys.argv[i])
    print(answer)
