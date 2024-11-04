class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0 
        right = len(height) - 1
        most = 0
        while left < right:
            cur = min(height[left],height[right])*(right - left)
            most = max(most,cur)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return most