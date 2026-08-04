class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_map = {}
        max_length = 0
        

        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        for i in hash_map:
            if i + 1 in hash_map:
                temp = hash_map[i] + hash_map[i + 1]
                max_length = max(max_length, temp)
                
        return max_length
