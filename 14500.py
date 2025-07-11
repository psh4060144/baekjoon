# 테트리미노

delta = [
    ((0, 0), (1, 0), (2, 0), (3, 0)),  # I 미노 - 1
    ((0, 0), (0, 1), (0, 2), (0, 3)),  # I 미노 - 2
    ((0, 0), (1, 0), (0, 1), (1, 1)),  # O 미노 - 1
    ((0, 0), (1, 0), (2, 0), (2, 1)),  # L 미노 - 1
    ((0, 0), (1, 0), (2, 0), (2, -1)),  # L 미노 - 2
    ((0, 0), (0, 1), (1, 0), (2, 0)),  # L 미노 - 3
    ((0, 0), (0, -1), (1, 0), (2, 0)),  # L 미노 - 4
    ((0, 0), (1, 0), (1, 1), (1, 2)),  # L 미노 - 5
    ((0, 0), (1, 0), (1, -1), (1, -2)),  # L 미노 - 6
    ((0, 0), (0, 1), (0, 2), (1, 0)),  # L 미노 - 7
    ((0, 0), (0, -1), (0, -2), (1, 0)),  # L 미노 - 8
    ((0, 0), (1, 0), (1, 1), (2, 1)),  # Z 미노 - 1
    ((0, 0), (1, 0), (1, -1), (2, -1)),  # Z 미노 - 2
    ((0, 0), (0, 1), (1, 1), (1, 2)),  # Z 미노 - 3
    ((0, 0), (0, -1), (1, -1), (1, -2)),  # Z 미노 - 4
    ((0, 0), (-1, 0), (0, 1), (1, 0)),  # T 미노 - 1
    ((0, 0), (0, 1), (1, 0), (0, -1)),  # T 미노 - 2
    ((0, 0), (1, 0), (0, -1), (-1, 0)),  # T 미노 - 3
    ((0, 0), (0, -1), (-1, 0), (0, 1)),  # T 미노 - 4
]

N, M = map(int, input().split())  # 세로 N, 가로 M
field = [list(map(int, input().split())) for _ in range(N)]
sum_max = 0

for r in range(N):
    for c in range(M):
        for i in range(19):
            r1, c1 = r + delta[i][1][0], c + delta[i][1][1]
            r2, c2 = r + delta[i][2][0], c + delta[i][2][1]
            r3, c3 = r + delta[i][3][0], c + delta[i][3][1]
            if 0 <= r1 < N and 0 <= r2 < N and 0 <= r3 < N and 0 <= c1 < M and 0 <= c2 < M and 0 <= c3 < M:
                tetra_sum = field[r][c] + field[r1][c1] + field[r2][c2] + field[r3][c3]
                if sum_max < tetra_sum:
                    sum_max = tetra_sum

print(sum_max)