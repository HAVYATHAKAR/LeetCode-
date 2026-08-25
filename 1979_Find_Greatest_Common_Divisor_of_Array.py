class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a,b=max(nums),min(nums)
        while b:
            a,b=b,a%b
        return a

        
