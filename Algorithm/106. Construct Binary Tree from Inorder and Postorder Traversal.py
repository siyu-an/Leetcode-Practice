class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        mapping = {}
        for i in range(len(inorder)):
            mapping[inorder[i]] = i
        def build(start, end):
            if start > end:
                return None
            root = TreeNode(postorder.pop())
            mid = mapping[root.val]
            root.right = build(mid+1,end)
            root.left = build(start,mid - 1)
            return root
        return build(0,len(inorder)-1)