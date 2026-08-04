class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        sorted_score = sorted(score, reverse=True)

        rank_map = {}
        for i in range(len(sorted_score)):
            if i == 0:
                rank_map[sorted_score[i]] = "Gold Medal"
            elif i == 1:
                rank_map[sorted_score[i]] = "Silver Medal"
            elif i == 2:
                rank_map[sorted_score[i]] = "Bronze Medal"
            else:
                rank_map[sorted_score[i]] = str(i + 1)

        result = []
        for s in score:
            result.append(rank_map[s])
            
        return result
