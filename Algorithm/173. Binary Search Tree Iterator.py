class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self.curr_index = 0
        self.in_order(root)
    
    def in_order(self,root):
        if not root:
            return None
        self.in_order(root.left)
        self.arr.append(root.val)
        self.in_order(root.right)

        

    def next(self) -> int:
        val = self.arr[self.curr_index]
        self.curr_index += 1
        return val
        

    def hasNext(self) -> bool:
        return self.curr_index < len(self.arr)