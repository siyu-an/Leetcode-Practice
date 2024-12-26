class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        next_level = deque([root])
        ans = []
        while next_level:
            leafs = []
            count = len(next_level)
            while count:
                node = next_level.popleft()
                leafs.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                count -= 1
            ans.append(leafs)
        return ans