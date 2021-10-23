N = 9


def output_file(a):
    with open('output.txt', 'r+') as file:
        for i in range(N):
            for j in range(N):
                print(a[i][j], end=" ")
                grid[i][j] = str(grid[i][j])
                file.write(a[i][j])
            file.write('\n')
            print()


def rowcol(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False

    for x in range(9):
        if grid[x][col] == num:
            return False

    start_Row = row - row % 3
    start_Col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_Row][j + start_Col] == num:
                return False
    return True


def solution(grid, row, col):
    if row == N - 1 and col == N:
        return True
    if col == N:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return solution(grid, row, col + 1)
    for num in range(1, N + 1, 1):
        if rowcol(grid, row, col, num):
            grid[row][col] = num
            if solution(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False


with open('input.txt') as file:
    field = enumerate(file.read().splitlines())
    grid = list()
    for index, element in field:
        grid.append(list(element))
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] = int(grid[i][j])

if solution(grid, 0, 0):
    output_file(grid)
else:
    print("Impossible")
