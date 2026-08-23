class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        right = 0
        mx = 0
        fre = {}

        while right < len(s):
            if s[right] not in fre:
                fre[s[right]] = 1
            else:
                fre[s[right]] += 1

            while fre[s[right]] > 1:
                fre[s[left]] -= 1
                left += 1

            mx = max(mx, right - left + 1)
            right += 1

        return mx
