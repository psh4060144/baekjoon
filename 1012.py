delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상우하좌

def dfs(a, b):
    global visited, earthworm
    stack = []
    if not visited[a][b] and field[a][b]:
        stack.append((a, b))
        visited[a][b] = 1

        while stack:
            cr, cc = stack[-1]
            for i in range(4):
                rr, rc = cr + delta[i][0], cc + delta[i][1]
                if 0 <= rr < N and 0 <= rc < M and field[rr][rc] and not visited[rr][rc]:
                    stack.append((rr, rc))
                    visited[rr][rc] = 1
                    break
            else:
                stack.pop()

        earthworm += 1

T = int(input())
for tc in range(1, T + 1):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    for i in range(K):
        c, r = map(int, input().split())
        field[r][c] = 1

    visited = [[0] * M for _ in range(N)]
    earthworm = 0
    for j in range(N):
        for k in range(M):
            dfs(j, k)

    print(earthworm)