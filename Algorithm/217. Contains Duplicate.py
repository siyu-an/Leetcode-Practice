# 217. Contains Duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums))<len(nums)

#or
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic={}
        for i in nums:
            if i in dic:
                return True
            else:
                dic[i] = 1
        return False
