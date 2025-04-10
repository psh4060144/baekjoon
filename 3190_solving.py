direction = {'u': (-1, 0), 'r': (0, 1), 'd': (1, 0), 'l': (0, -1)}
delta = ['u', 'r', 'd', 'l']
left = ['l', 'u', 'r', 'd']
right = ['r', 'd', 'l', 'u']


def game():
    head = (0, 0)
    tail = (0, 0)
    length = 1
    current = delta[1]
    snake = [head, tail, length, current]

    while True:
        new_head = (head[0] + direction[current][0], head[1] + direction[current][1])



N = int(input())

field = [[0] * N for _ in range(N)]
cr, cc = 0, 0
field[cr][cc] = 1

K = int(input())
for _ in range(K):
    r, c = map(int, input().split())
    field[r][c] = 5

L = int(input())
timeline = []
for _ in range(L):
    X, C = input().split()
    timeline.append((int(X), C))

