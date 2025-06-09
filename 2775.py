# 부녀회장이 될 테야

T = int(input())
for _ in range(T):

    k = int(input()) + 1
    n = int(input()) + 1
    apt = [[0] * n for _ in range(k)]

    for i in range(k):
        for j in range(1, n):
            if i == 0:
                apt[i][j] = j
            else:
                apt[i][j] = apt[i - 1][j] + apt[i][j - 1]

    print(apt[k - 1][n - 1])