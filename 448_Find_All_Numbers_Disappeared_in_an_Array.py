class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = dict.fromkeys(range(1, len(nums) + 1), 0)
        
        
        for num in nums:
            temp[num] += 1
            
        
        templ = [key for key, val in temp.items() if val == 0]
        return templ
