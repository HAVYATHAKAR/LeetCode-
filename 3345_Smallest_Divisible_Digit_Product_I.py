class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        i = n
        while True:
            mul = 1 
            st = str(i)
            for j in st:
                mul *= int(j) 

            if mul % t == 0:
                return i
            i += 1
