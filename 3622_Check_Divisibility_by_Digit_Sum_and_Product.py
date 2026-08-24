class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        l = list(map(int, str(n)))
        total = 0
        prod = 1
        for i in range(len(l)): total += l[i]
        for i in range(len(l)): prod *= l[i]

        if (n% (total + prod)) == 0:
            return True
        else:
            return False 
