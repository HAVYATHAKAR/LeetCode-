class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s1=set(nums1)
        s2=set(nums2)
        temp=[]
        if len(s1)>=len(s2):
            for i in s2:
                if i in s1:
                    temp.append(i)
        else:
            for i in s1:
                if i in s2:
                    temp.append(i)
        return temp
