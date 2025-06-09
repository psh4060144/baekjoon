# 듣보잡

N, M = map(int, input().split())
names = set()

for i in range(N):
    name = input()
    names.add(name)

infamous = []
for j in range(M):
    name = input()
    if name in names:
        infamous.append(name)

infamous.sort()
print(len(infamous))
for k in range(len(infamous)):
    print(infamous[k])