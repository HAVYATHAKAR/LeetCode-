class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)

        # Only one subarray exists
        if k == n:
            return max(nums)

        ans = -1

        # Check elements that can belong to exactly one window
        for x in set(nums):

            count = 0

            # Check every subarray of size k
            for i in range(n - k + 1):
                if x in nums[i:i+k]:
                    count += 1

            if count == 1:
                ans = max(ans, x)

        return ans
