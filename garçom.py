

N = int(input())#bandejas

copos = 0
for i in range(N):
    L, C = input().split()
    L = int(L)
    C = int(C)
    if L > C:
        copos += C

print(copos)
