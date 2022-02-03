#696. Count Binary Substrings
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        # I used count to count the total qualified substrings
        # prev is the location of previous group endpoint and follow is the following group endpoint
        # each group consists of eithe '0's or '1's and two adjacent groups are different
        # diff1 represents the length of previous group and diff2 represents the length of the following group
        count = 0
        prev = 0
        diff1 = 0
        follow = 0
        for i in range(len(s) - 1):
            # if two contiguous characters are different, it means the group changes
            # then we can take the minimum length of two groups to know how many substrings are qualified
            if s[i] != s[i + 1]:
                follow = i + 1
                diff2 = follow - prev
                count += min(diff1, diff2)
                diff1 = diff2
                prev = follow
        # if s only consists of only '0' or '1', return 0
        if follow == 0:
            return 0
        # sum of all counts
        count += min(len(s) - follow, diff1)
        return count
