class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mapping = {}
        for i in range(len(preorder)):
            mapping[inorder[i]] = i
        preorder = collections.deque(preorder)
        def build(start,end):
            if start > end: return None
            root = TreeNode(preorder.popleft())
            mid = mapping[root.val]
            root.left = build(start, mid - 1)
            root.right = build(mid + 1, end)
            return root
        return build(0,len(preorder) - 1)
