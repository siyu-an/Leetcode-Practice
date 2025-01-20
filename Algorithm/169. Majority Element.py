class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #count = 0
        #res = nums[0]
        #hash_map = defaultdict(int)
        #for num in nums:
        #    hash_map[num] += 1
        #    if hash_map[num] > count:
        #        count = hash_map[num]
        #        res = num
        #return res
        nums.sort()
        return nums[len(nums) // 2]