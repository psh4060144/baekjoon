# 아기 상어

delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상우하좌


def bfs(x, y):
    global field, size, eat_cnt
    queue = [(x, y, 0)]
    field[x][y] = 0
    visited = [[0] * N for _ in range(N)]
    visited[x][y] = 1
    container = 0

    while queue:
        cr, cc, cm = queue.pop(0)
        for i in range(4):
            nr, nc = cr + delta[i][0], cc + delta[i][1]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if field[nr][nc] == 0 or field[nr][nc] == size:
                    queue.append((nr, nc, cm + 1))
                    visited[nr][nc] = 1
                elif field[nr][nc] < size:
                    if not container:
                        container = (nr, nc, cm + 1)
                    else:
                        if cm + 1 <= container[2] and nr <= container[0] and nc <= container[1]:
                            container = (nr, nc, cm + 1)
                    visited[nr][nc] = 1

    if container:
        eat_cnt += 1
        if size == eat_cnt:
            size += 1
            eat_cnt = 0
        field[container[0]][container[1]] = 9
        return container[2]
    return container


N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]

size = 2
eat_cnt = 0
path = 0

while True:
    flag = 0
    for i in range(N):
        if flag:
            break
        for j in range(N):
            if field[i][j] == 9:
                baby_shark = (i, j)
                flag = 1
                break
    result = bfs(baby_shark[0], baby_shark[1])
    if result == 0:
        break
    else:
        path += result

print(path)