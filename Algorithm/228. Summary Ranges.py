class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [f'{nums[0]}']
        start = 0
        end = 0
        result = []
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                end += 1
            else:
                if end > start:
                    result.append(f'{nums[start]}->{nums[end]}')
                else:
                    result.append(f'{nums[start]}')
                start = end = i+1
        if start == end:
            result.append(f'{nums[start]}')
        else:
            result.append(f'{nums[start]}->{nums[end]}')
        return result
