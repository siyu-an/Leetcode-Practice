class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = collections.deque([root])
        dummy = Node(0)
        while q:
            length = len(q)
            prev = dummy
            for _ in range(length):
                v = q.popleft()
                if v.left:
                    q.append(v.left)
                    prev.next = v.left
                    prev = prev.next
                if v.right:
                    q.append(v.right)
                    prev.next = v.right
                    prev = prev.next
        return root