inp = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 04\input6.txt", "r")
out = open("F:\BRACU\CSE221\Lab Assignments of Spring2024\Lab 04\output6.txt", "w")


def floodFill(grid, row, col, vis, i, j):
    if i < 0 or j<0 or j >= col or i >= row or grid[i][j] == "#"  or vis[i][j] == 1:
        return 0
    vis[i][j] = 1
    dd = 0
    if grid[i][j] == "D":
        dd = 1
    dd += floodFill(grid, row, col, vis,  i, j+1) + floodFill(grid, row, col, vis, i, j-1) + floodFill(grid, row, col, vis, i-1, j) + floodFill(grid, row, col, vis,i+1, j)
    return dd


# Input 01
row, col = list(map(int, inp.readline().split()))
grid = []
for i in range(row):
    grid.append(list(inp.readline().strip()))
vis = []
for  _ in range(row):
    r = [0]*col
    vis.append(r)
dmond = 0
for i in range(row):
    for j in range(col):
        # if  grid[i][j] != "D":
            temp = floodFill(grid, row, col, vis, i, j)
            dmond = max(temp, dmond)
out.write(f"Output 01\n {dmond}\n")

# Input 02
row, col = list(map(int, inp.readline().split()))
grid = []
for i in range(row):
    grid.append(list(inp.readline().strip()))
vis = []
for  _ in range(row):
    r = [0]*col
    vis.append(r)
dmond = 0
for i in range(row):
    for j in range(col):
        if  grid[i][j] != "D":
            temp = floodFill(grid, row, col, vis, i, j)
            dmond = max(temp, dmond)
out.write(f"Output 02\n {dmond}\n")

# Input 03
row, col = list(map(int, inp.readline().split()))
grid = []
for i in range(row):
    grid.append(list(inp.readline().strip()))
vis = []
for  _ in range(row):
    r = [0]*col
    vis.append(r)
dmond = 0
for i in range(row):
    for j in range(col):
        if  grid[i][j] != "D":
            temp = floodFill(grid, row, col, vis, i, j)
            dmond = max(temp, dmond)
out.write(f"Output 03\n {dmond}\n")

# Input 04
row, col = list(map(int, inp.readline().split()))
grid = []
for i in range(row):
    grid.append(list(inp.readline().strip()))
vis = []
for  _ in range(row):
    r = [0]*col
    vis.append(r)
dmond = 0
for i in range(row):
    for j in range(col):
        if  grid[i][j] != "D":
            temp = floodFill(grid, row, col, vis, i, j)
            dmond = max(temp, dmond)
out.write(f"Output 04\n {dmond}\n")

# Input 05
row, col = list(map(int, inp.readline().split()))
grid = []
for i in range(row):
    grid.append(list(inp.readline().strip()))
vis = []
for  _ in range(row):
    r = [0]*col
    vis.append(r)
dmond = 0
for i in range(row):
    for j in range(col):
        if  grid[i][j] != "D":
            temp = floodFill(grid, row, col, vis, i, j)
            dmond = max(temp, dmond)
out.write(f"Output 05\n {dmond}\n")

# Input 06
row, col = list(map(int, inp.readline().split()))
grid = []
for i in range(row):
    grid.append(list(inp.readline().strip()))
vis = []
for  _ in range(row):
    r = [0]*col
    vis.append(r)
dmond = 0
for i in range(row):
    for j in range(col):
        if  grid[i][j] != "D":
            temp = floodFill(grid, row, col, vis, i, j)
            dmond = max(temp, dmond)
out.write(f"Output 06\n {dmond}\n")

# Input 07
row, col = list(map(int, inp.readline().split()))
grid = []
for i in range(row):
    grid.append(list(inp.readline().strip()))
vis = []
for  _ in range(row):
    r = [0]*col
    vis.append(r)
dmond = 0
for i in range(row):
    for j in range(col):
        if  grid[i][j] != "D":
            temp = floodFill(grid, row, col, vis, i, j)
            dmond = max(temp, dmond)
out.write(f"Output 07\n {dmond}\n")


inp.close()
out.close()