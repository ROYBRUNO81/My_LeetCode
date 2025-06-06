def kthSmallest(root, k):
    """
    :type root: Optional[TreeNode]
    :type k: int
    :rtype: int
    """
    inorder = []
    def dfs(node):
        if node.left:
            dfs(node.left)
        inorder.append(node.val)
        if node.right:
            dfs(node.right)

    dfs(root)
    return inorder[k-1]