class Solution(object):
    def longestSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_xor = 0
        nzcount = 0
        for i in nums:
            total_xor = total_xor ^ i
            if i > 0:
                nzcount += 1

        if nzcount == 0:
            return 0
        else:
            if total_xor == 0:
                return len(nums)-1
            else:
                return len(nums)
