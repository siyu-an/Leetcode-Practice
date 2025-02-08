class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        mono_stack = []
        for i in range(n):
            if not mono_stack or nums[mono_stack[-1]] > nums[i]:
                mono_stack.append(i)
        max_width = 0
        for j in range(n-1,-1,-1):
            while mono_stack and nums[mono_stack[-1]] <= nums[j]:
                max_width = max(max_width, j - mono_stack[-1])
                mono_stack.pop()
        return max_width