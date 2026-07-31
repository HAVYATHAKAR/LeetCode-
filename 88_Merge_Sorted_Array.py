class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if n == 0:
            return

        for i in range(n):
            nums1[m + i] = nums2[i]

        nums1.sort()
