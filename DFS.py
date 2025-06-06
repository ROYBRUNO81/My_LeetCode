def exist(self, board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    Adj_list = {}
    m = len(board)
    n = len(board[0])
    visited = {}
    sources = []
    end = len(word)
    for i in range(m):
        for j in range(n):
            v = board[i][j] + str(i) + str(j)
            neighbors = []
            if(i+1 < m):
                neighbors.append(board[i+1][j] + str(i+1) + str(j))
            if(i-1 >= 0):
                neighbors.append(board[i-1][j] + str(i-1) + str(j))
            if(j+1 < n):
                neighbors.append(board[i][j+1] + str(i) + str(j+1))
            if(j-1 >= 0):
                neighbors.append(board[i][j-1] + str(i) + str(j-1))
            Adj_list[v] = neighbors
            visited[v] = False

            if(board[i][j] == word[0]):
                sources.append(v)
    
    def DFS_visit(v, i):
        for u in Adj_list[v]:
            if u[0] == word[i] and visited[u] == False:
                i += 1
                visited[u] == True
                if i == end:
                    return true
            DFS_visit(u, i)
        visited[v] == False

    
    for s in sources:
        visited[s] == True
        i = 1
        DFS_visit(s, i)


    return len(Adj_list[board[0][0]])