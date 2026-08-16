class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        min_num = min(nums)
        max_num = max(nums)
        num_set = set(nums)
        return [num for num in range(min_num + 1, max_num) if num not in num_set]
