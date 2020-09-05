from itertools import combinations
import sys
input = lambda : sys.stdin.readline().rstrip()

kk =True


while kk:
    a = list(map(int,input().split()))
    if a[0] == 0:
        kk=False
        break


    combList = list((combinations(a[1:],6)))


    for i in combList :
        print(" ".join(map(str,i)))
    print()