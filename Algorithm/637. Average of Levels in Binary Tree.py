class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        next_level = deque([root])
        avg = []
        while next_level:
            curr_level = next_level
            val = []
            next_level = deque()
            while curr_level:
                node = curr_level.popleft()
                val.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            avg.append(sum(val)/len(val))
        return avg