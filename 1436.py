# 영화감독 숌

N = int(input())
start = 665
count = 0

while True:
    start += 1
    if '666' in str(start):
        count += 1
    if count == N:
        break

print(start)