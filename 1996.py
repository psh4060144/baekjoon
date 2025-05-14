# 지뢰찾기

delta = [
    (-1, 0), (-1, 1), (0, 1), (1, 1),
    (1, 0), (1, -1), (0, -1), (-1, -1),
]  # 위쪽부터 시계방향 8방향

N = int(input())
field = [list(input()) for _ in range(N)]
new_field = [[0] * N for _ in range(N)]

for row in range(N):
    for col in range(N):
        if field[row][col] != '.':
            new_field[row][col] = '*'
            pass
        else:
            for dl in range(8):
                nr, nc = row + delta[dl][0], col + delta[dl][1]
                if 0 <= nr < N and 0 <= nc < N and field[nr][nc] != '.':
                    new_field[row][col] += int(field[nr][nc])
            if new_field[row][col] >= 10:
                new_field[row][col] = 'M'

for i in range(N):
    for j in range(N):
        print(new_field[i][j], end='')
    print()
