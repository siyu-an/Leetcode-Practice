class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(x):
            left = 0 
            right = len(nums)
            while left < right:
                mid = (left + right) // 2
                if nums[mid] < x:
                    left = mid + 1
                else:
                    right = mid
            return left
        lo = search(target)
        hi = search(target+1)-1
        if lo <= hi:
            return [lo,hi]
        return [-1,-1]
