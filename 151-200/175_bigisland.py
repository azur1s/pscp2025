"""a"""
y, x = map(int, input().split())
board = [input().split(" ") for _ in range(y)]

dirs = [
    (1, 0), (-1, 0), (0, 1), (0, -1),
    (1, 1), (1, -1), (-1, 1), (-1, -1),
]
visited = [[0] * x for _ in range(y)]
sizes = []

for row in range(y):
    for col in range(x):
        if board[row][col] == '1' and not visited[row][col]:
            stack = [(row, col)]
            visited[row][col] = 1
            CURRENT_SIZE = 0

            while stack:
                cy, cx = stack.pop()
                CURRENT_SIZE += 1

                for dy, dx in dirs:
                    ny, nx = cy + dy, cx + dx

                    if 0 <= ny < y and 0 <= nx < x:
                        if board[ny][nx] == '1' and not visited[ny][nx]:
                            visited[ny][nx] = 1
                            stack.append((ny, nx))
            sizes.append(CURRENT_SIZE)

print(max(sizes) if sizes else 0)
