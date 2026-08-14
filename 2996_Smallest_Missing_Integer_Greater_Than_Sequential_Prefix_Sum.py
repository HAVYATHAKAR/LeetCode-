class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        total = nums[0]
        
        # Find sum of longest consecutive prefix
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break
        
        # Find the smallest integer >= total that is not in nums
        while total in nums:
            total += 1
        
        return total
