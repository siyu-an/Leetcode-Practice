class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cur, stack = root, []
        d = 0
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            d += 1
            if d == k:
                return node.val
            cur = node.right