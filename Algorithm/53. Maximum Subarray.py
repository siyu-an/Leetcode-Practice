#53. Maximum Subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # initialize current subarray sum and maximum of the sum as first element in the array
        current_max=subarray_max=nums[0]
        # for every element in the following array, if it is greater than previous sum (current_max)
        # we set current_max as the element; otherwise, we add it to the current_max to get a bigger sum
        # then update subarray_max
        for num in nums[1:]:
            current_max=max(num,current_max+num)
            subarray_max=max(current_max,subarray_max)
        return subarray_max
