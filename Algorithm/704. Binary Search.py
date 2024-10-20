# 704. Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # initialize left and right pointer at the start and the end
        left, right = 0, len(nums) - 1
        while left <= right:
            # find the middle point
            pivot = left + (right - left) // 2
            # if middle point is equal to target then return index
            if nums[pivot] == target:
                return pivot
            # if target is larger than middel point then it must be in
            # the right part of the array
            if nums[pivot] < target:
                left = pivot + 1
            # otherwise, it must be in the left part
            else :
                right = pivot -1
        # if can't find such number return -1
        return -1