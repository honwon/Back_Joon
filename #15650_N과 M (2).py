from itertools import combinations

N, M= map(int,input().split())
L = []
for i in range(N):
    L.append(i+1)

A = list(combinations(L,M))
for i in A:
    for j in i:
        print(j,end=" ")
    print()