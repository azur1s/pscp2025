"""a"""
y, x = map(int, input().split())
board = [input().split(" ") for _ in range(y)]

dirs = [
    (1, 0), (-1, 0), (0, 1), (0, -1),
    (1, 1), (1, -1), (-1, 1), (-1, -1),
]
visited = [[0] * x for _ in range(y)]
COUNT = 0

for row in range(y):
    for col in range(x):
        if board[row][col] == '1' and not visited[row][col]:
            stack = [(row, col)]
            visited[row][col] = 1

            while stack:
                cy, cx = stack.pop()

                for dy, dx in dirs:
                    ny, nx = cy + dy, cx + dx

                    if 0 <= ny < y and 0 <= nx < x:
                        if board[ny][nx] == '1' and not visited[ny][nx]:
                            visited[ny][nx] = 1
                            stack.append((ny, nx))
            COUNT += 1

print(COUNT)
