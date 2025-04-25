# 1, 2, 3 더하기

T = int(input())

memo = [0] * 11
memo[0] = 1
memo[1] = 2
memo[2] = 4

for i in range(3, 11):
    memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]

for t in range(T):
    print(memo[int(input())-1])
