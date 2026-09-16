class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)

        ones = []

        # Store coordinates of 1s in img1
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    ones.append((i, j))

        ans = 0

        # Try every possible shift
        for dr in range(-n + 1, n):
            for dc in range(-n + 1, n):
                count = 0

                for r, c in ones:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < n and 0 <= nc < n:
                        if img2[nr][nc] == 1:
                            count += 1

                ans = max(ans, count)

        return ans
