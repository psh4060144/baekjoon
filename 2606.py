# 바이러스

def bfs(start):
    count = 0
    queue = [start]
    visited = [0] * n
    visited[start] = 1

    while queue:
        current = queue.pop(0)
        for i in range(n):
            if field[i][current] and not visited[i]:
                queue.append(i)
                visited[i] = 1
                count += 1

    return count


n = int(input())
e = int(input())
field = [[0] * n for _ in range(n)]

for i in range(e):
    r, c = map(int, input().split())
    field[r - 1][c - 1] = 1
    field[c - 1][r - 1] = 1

result = bfs(0)
print(result)