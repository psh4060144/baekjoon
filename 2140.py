# 지뢰찾기

delta = [
    (-1, 0), (-1, 1), (0, 1), (1, 1),
    (1, 0), (1, -1), (0, -1), (-1, -1),
]  # 위부터 시계방향으로 8방향

N = int(input())
field = [list(input()) for _ in range(N)]
count = 0

if N in (1, 2):
    print(count)

else:
    for i in range(N):
        for j in range(N):
            if field[i][j] != '#':
                field[i][j] = int(field[i][j])

    for r in range(N):
        for c in range(N):
            if field[r][c] == '#':
                for dl in range(8):
                    nr, nc = r + delta[dl][0], c + delta[dl][1]
                    if field[nr][nc] == 0:
                        break
                else:
                    for dl in range(8):
                        nr, nc = r + delta[dl][0], c + delta[dl][1]
                        if field[nr][nc] != '#':
                            field[nr][nc] -= 1
                    count += 1

    print(count)
