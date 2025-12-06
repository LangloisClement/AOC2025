from pkg_resources import resource_stream


grid: list[list[str]] = []
with resource_stream("input", "inputD4.txt") as textInput:
    for line in textInput.readlines():
        line = line.decode().strip()
        grid.append(list(line))
L, C = len(grid), len(grid[0])


def get_neighbor(line: int, col: int):
    neighbors = 0
    for i in [line - 1, line, line + 1]:
        if i < 0 or i >= L:
            continue
        for j in [col - 1, col, col + 1]:
            if j < 0 or j >= C:
                continue
            if i == line and j == col:
                continue
            neighbors += 1 if grid[i][j] == "@" else 0
    return neighbors


def part1():
    memo = 0
    for i in range(L):
        for j in range(C):
            if grid[i][j] == ".":
                continue
            memo += 1 if get_neighbor(i, j) < 4 else 0
    return memo
