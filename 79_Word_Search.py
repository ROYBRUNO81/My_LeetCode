def exist(board, word):
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
        if i == end:
            return True
        for u in Adj_list[v]:
            if u[0] == word[i] and visited[u] == False:
                visited[u] = True
                if DFS_visit(u, i+1) == True:
                    return True
                visited[v] = False
        return False


    for s in sources:
        visited[s] = True
        if DFS_visit(s, 1):
            return True
        visited[s] = False

    return False

board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
word = "ABCESEEEFS"
print(exist(board, word))