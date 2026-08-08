class Solution(object):
    def duplicateZeros(self, arr):
        result = []

        for x in arr:
            result.append(x)

            if x == 0:
                result.append(0)

        arr[:] = result[:len(arr)]
