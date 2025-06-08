def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    adj = [[] for _ in range(numCourses)]
    for dest, src in prerequisites:
        adj[src].append(dest)

    # 0=unvisited, 1=visiting, 2=done
    color = [0] * numCourses

    # Cycle detectection dfs
    def dfs(u):
        color[u] = 1
        for v in adj[u]:
            if color[v] == 1:
                return False
            if color[v] == 0 and not dfs(v):
                return False
        color[u] = 2
        return True

    for u in range(numCourses):
        if color[u] == 0:
            if not dfs(u):
                return False

    return True

print(canFinish(2, [[1,0],[0,1]]))