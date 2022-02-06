# 938. Range Sum of BST
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # if the root in null return 0
        if not root:
            return 0
        # if the root is smaller than low then move root to the right node
        # and compute the sum of the new root
        elif root.val < low:
            return self.rangeSumBST(root.right, low, high)
        # similarly for the larger than high situation
        elif root.val > high:
            return self.rangeSumBST(root.left, low, high)
        # if the root isbetween low and high then add root.val to the total
        # and calculate the sum of its left node as root as well as its right node 
        else:
            return root.val+self.rangeSumBST(root.right, low, high)+self.rangeSumBST(root.left, low, high)