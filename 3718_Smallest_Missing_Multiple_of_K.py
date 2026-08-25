class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mul = 1
        while(True):
            if k*mul in nums:
                mul+=1
            else:
                return k*mul
                break
