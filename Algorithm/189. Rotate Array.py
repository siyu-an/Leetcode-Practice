class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k != 0:
            move_part = []
            move_part += nums[-k:]
            nums[k:len(nums)] = nums[0:len(nums)-k]
            nums[0:k] = move_part