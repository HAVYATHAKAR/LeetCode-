class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        arr1.sort()

        temp = []
        used = [False] * len(arr1)

        for x in arr2:
            for i in range(len(arr1)):
                if arr1[i] == x:
                    temp.append(arr1[i])
                    used[i] = True

        for i in range(len(arr1)):
            if not used[i]:
                temp.append(arr1[i])

        return temp
