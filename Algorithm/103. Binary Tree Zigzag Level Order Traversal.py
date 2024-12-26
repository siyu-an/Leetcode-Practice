class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        curr_level = deque([root])
        ans = []
        d = 0
        while curr_level:
            val = deque()
            count = len(curr_level)
            while count:
                node = curr_level.popleft()
                if d % 2 == 0:
                    val.append(node.val)
                else:
                    val.appendleft(node.val)
                if node.left:
                    curr_level.append(node.left)
                if node.right:
                    curr_level.append(node.right)
                count -= 1
            d += 1
            ans.append(list(val))
        return ans