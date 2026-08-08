class Solution(object):
    def heightChecker(self, heights):
        expected = heights[:]
        expected.sort()

        count = 0
        i = 0

        while i < len(heights):
            if heights[i] != expected[i]:
                count += 1
            i += 1

        return count
