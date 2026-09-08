class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_dict = {}
        max_len = 0
        left = 0

        for right in range(len(s)):
            if s[right] in my_dict and my_dict[s[right]] >= left:
                left = my_dict[s[right]] + 1

            my_dict[s[right]] = right

            max_len = max(max_len, right - left + 1)
        return max_len