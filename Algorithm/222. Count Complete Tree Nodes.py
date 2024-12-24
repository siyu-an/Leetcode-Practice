class Solution:
    def max_depth(self, node:TreeNode) -> int:
        d = 0
        while node.left:
            node = node.left
            d += 1
        return d
    def existence(self, idx: int, d: int, node: TreeNode) -> bool:
        left, right = 0, 2**d - 1
        for _ in range(d):
            pivot = left + (right - left) // 2
            if idx <= pivot:
                node = node.left
                right = pivot
            else:
                node = node.right
                left = pivot + 1
        return node is not None

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        d = self.max_depth(root)
        left, right = 0, 2**d - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if self.existence(pivot, d, root):
                left = pivot + 1
            else:
                right = pivot - 1
        return (2**d - 1) + left