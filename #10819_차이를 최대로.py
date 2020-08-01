# 중복 없는 순열
from itertools import permutations

n= int(input())
a = list(map(int,input().split()))

big =0
b= list(permutations(a,n))

for i in b:
    c=0
    for j in range(len(i)):
        if (j == len(i)-1):
            continue
        else: c += abs(i[j]-i[j+1])
        big = max(big, c)


print(big)


