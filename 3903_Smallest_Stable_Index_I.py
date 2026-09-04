class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        lst = []
        for i in range(len(nums)):
            mx = max(nums[0:i+1])
            mn = min(nums[i:])
            if (mx - mn) <= k:
                lst.append(i)
        
        if lst==[]:
            return -1
        else:
            return min(lst)
