class Solution(object): 
    def uniformArray(self, nums1): 
        """ 
        :type nums1: List[int] 
        :rtype: bool 
        """ 
        allodd = True 
        alleven = True 

        for i in nums1: 
            if i%2 == 0: 
                allodd = False 
            else: 
                alleven = False
            
        if alleven == True:
            return True 
 
        odd = min(i for i in nums1 if i % 2 != 0)

        if alleven == False and allodd == False:

            for i in nums1:
                if i % 2 == 0:
                    if odd >= i:
                        return False

        return True
