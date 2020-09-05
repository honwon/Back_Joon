from itertools import combinations
import sys

input = lambda : sys.stdin.readline().rstrip()

dirtyList=[]

number, count = list(map(int,input().split()))
mixList = []
for i in range(number):
    mixList.append(i+1)


for i in range(count):
    dirtyList.append(list(map(int, input().split())))
print(dirtyList)
combList = list(combinations(mixList,count))
for i in combList:
    uu = []
    for j in i:
        uu.append(j)
        if(uu.count(1) >0 and uu.count(2)>0 or uu.count(3)>0 and uu.count(4)>0 or uu.count(1)>0 and uu.count(3)>0 ):
            continue
        print(uu)

