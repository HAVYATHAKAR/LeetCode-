class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp=[]
        hash_map={}
        n= len(nums)
        for i in range(0,n):
            hash_map[nums[i]]=hash_map.get(nums[i],0)+1
        for j in nums:
            if hash_map.get(j)>(n/3):
                temp.append(j)
        return list(set(temp))
