def findMinHeightTrees(n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: List[int]
    """

    adj_list = []
    visited = []
    for i in range(n):
        adj_list.append([])
        visited.append(False)

    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])

    leafs = []
    for i in range(n):
        if len(adj_list[i]) <= 1:
            leafs.append(i)

    curr_leafs = leafs
    while curr_leafs:
        leafs = curr_leafs
        next_leafs = []
        for v in curr_leafs:
            if adj_list[v]:
                adj_list[adj_list[v][0]].remove(v)
                if len(adj_list[adj_list[v][0]]) == 1:
                    next_leafs.append(adj_list[v][0])
        curr_leafs = next_leafs

    return leafs

print(findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))