import sys
input = lambda : sys.stdin.readline().rstrip()
a = int(input())
b= []
for i in range(a):
    cmd = input().split()
    if(cmd[0] == "push"):
        b.append(cmd[1])
    elif (cmd[0] == "top"):
        if (len(b) !=0):
            print(b[-1])
        else: print(-1)
    elif (cmd[0] == "size"):
        print(len(b))
    elif (cmd[0] == "empty"):
        if (len(b) !=0):
            print(0)
        else: print(1)
    elif (cmd[0] == "pop"):
        if (len(b) !=0):
            print(b[-1])
            b.pop()
        else: print(-1)