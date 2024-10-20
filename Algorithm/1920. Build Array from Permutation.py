#1920. Build Array from Permutation
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        q = len(nums)
        for i,c in enumerate(nums):
            nums[i] += q * (nums[c] % q)
        for i in range(q):
            nums[i] = nums[i] //q
        return nums
                