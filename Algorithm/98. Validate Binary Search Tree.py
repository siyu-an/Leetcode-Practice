class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        cur, stack = root, []
        prev = float('-inf')
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            if node.val <= prev:
                return False
            prev = node.val
            cur = node.right
        return True
