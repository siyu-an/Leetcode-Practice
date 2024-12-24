from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque([root,root])
        while q:
            t1 = q.popleft()
            t2 = q.popleft()
            if not t1 and not t2:
                continue
            if not t1 or not t2 or t1.val != t2.val:
                return False
            q.extend([t1.left,t2.right,t1.right,t2.left])
        return True