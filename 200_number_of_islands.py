def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    m = len(grid)
    n = len(grid[0])
    adj_list = {}
    visited = {}
    parent = {}

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                v = (i,j)
                neighbors = []
                if (i+1 < m) and grid[i+1][j] == "1":
                    neighbors.append((i+1,j))
                if(i-1 >= 0) and grid[i-1][j] == "1":
                    neighbors.append((i-1,j))
                if(j+1 < n) and grid[i][j+1] == "1":
                    neighbors.append((i,j+1))
                if(j-1 >= 0) and grid[i][j-1] == "1":
                    neighbors.append((i,j-1))

                adj_list[v] = neighbors
                visited[v] = False
                parent[v] = None

    def dfs(v):
        for u in adj_list[v]:
            if not visited[u]:
                parent[u] = v
                visited[u] = True
                dfs(u)
    count = 0
    for v in adj_list:
        if not visited[v]:
            count += 1
            visited[v] = True
            dfs(v)

    return count

grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]

print(numIslands(grid))