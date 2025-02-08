class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2,nums1)
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        while left <= right:
            partitionA = (left + right) // 2
            partitionB = (m + n + 1) // 2 - partitionA
            maxleftA = (float('-inf') if partitionA == 0 else nums1[partitionA - 1])
            minrightA = (float('inf') if partitionA == m else nums1[partitionA])
            maxleftB = (float('-inf') if partitionB == 0 else nums2[partitionB - 1])
            minrightB = (float('inf') if partitionB == n else nums2[partitionB])
            if maxleftA <= minrightB and maxleftB <= minrightA:
                if (m + n) % 2 == 0:
                    return (max(maxleftA, maxleftB) + min(minrightA, minrightB)) / 2
                else:
                    return max(maxleftA, maxleftB)
            elif maxleftA > minrightB:
                right = partitionA - 1
            else:
                left = partitionA + 1