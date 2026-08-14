class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_counts = {}
        max_length = 0
        left = 0
        
        # Expand the window using the right pointer
        for right in range(len(s)):
            current_char = s[right]
            char_counts[current_char] = char_counts.get(current_char, 0) + 1
            
            # Shrink the window from the left if any character occurs more than twice
            while char_counts[current_char] > 2:
                left_char = s[left]
                char_counts[left_char] -= 1
                left += 1
            
            # Update the maximum valid window length found so far
            current_length = right - left + 1
            if current_length > max_length:
                max_length = current_length
                
        return max_length
