# 중복 없는 순열
from itertools import permutations

n = int(input())
b = []
for i in range(n):
    b.append(i+1)
a= list(permutations(b,n))
for i in a:
    for j in i:
        print(j, end=" ")
    print()
