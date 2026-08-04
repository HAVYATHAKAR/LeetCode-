class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        # hash_map={}
        # for i in range(len(candyType)):
        #     hash_map[candyType[i]] = hash_map.get(candyType[i],0)+1
        # n = len(candyType)
        # m = len(hash_map)
        # if (n/2)<m:
        #     return (n/2)
        # else:
        #     return m
        return min((len(candyType)/2),(len(set(candyType))))
