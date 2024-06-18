def dfs(i, j, R, H, grid, visited):
    if i < 0 or i >= R or j < 0 or j >= H or grid[i][j] == '#' or visited[i][j]:
        return 0
    visited[i][j] = True
    dd = 0
    if grid[i][j] == 'D':
        dd = 1
    dd += dfs(i+1, j, R, H, grid, visited)
    dd += dfs(i-1, j, R, H, grid, visited)
    dd += dfs(i, j+1, R, H, grid, visited)
    dd += dfs(i, j-1, R, H, grid, visited)
    return dd

inp6 = open("input6.txt","r")
out6 = open("output6.txt","w")

line1 = inp6.readline().split(' ')

R = int(line1[0])
H = int(line1[1])

grid = []
for i in range(R):
  grid.append(inp6.readline().strip())



maxd = 0
visited = []
for i in range(R):
  visited.append([False] * H)

for i in range(R):
    for j in range(H):
        if grid[i][j] == 'D':
            dd = dfs(i, j, R, H, grid, visited)

            maxd = max(maxd, dd)

out6.write(str(maxd))

inp6.close()
out6.close()
