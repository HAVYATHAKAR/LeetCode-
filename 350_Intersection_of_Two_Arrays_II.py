class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s1=len(set(nums1))
        s2=len(set(nums2))
        temp=[]
        m=max(s1,s2)
        if s1 == max:
            for i in nums2:
                if i in nums1:
                    temp.append(i)
                    nums1.remove(i)
        else:
            for i in nums1:
                if i in nums2:
                    temp.append(i)
                    nums2.remove(i)
        return temp
