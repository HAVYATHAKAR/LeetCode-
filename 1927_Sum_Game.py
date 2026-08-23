class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        mid = n // 2

        left_half = num[:mid]
        right_half = num[mid:]

        sum_l = sum(int(c) for c in left_half if c.isdigit())
        count_l = left_half.count('?')

        sum_r = sum(int(c) for c in right_half if c.isdigit())
        count_r = right_half.count('?')

        if (count_l + count_r) % 2 != 0:
            return True
        if sum_l - sum_r == 9 * (count_r - count_l) // 2:
            return False
            
        return True
