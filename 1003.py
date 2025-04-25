# 피보나치 함수
T = int(input())
for t in range(T):
    N = int(input())
    memo = [0] * (N + 1)
    if N:
        memo[1] = 1
        if N > 1:
            for i in range(2, N + 1):
                memo[i] = memo[i - 1] + memo[i - 2]
    if N:
        print(memo[N - 1], end=' ')
    else:
        print(1, end=' ')
    print(memo[N])
