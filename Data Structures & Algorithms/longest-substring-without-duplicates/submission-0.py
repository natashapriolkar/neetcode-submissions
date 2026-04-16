class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        left = 0
        result = 0
        #Iterate over each character with a right pointer
        for right in range(len(s)):
            if s[right] in mp:
                left = max(mp[s[right]] + 1, left)

            mp[s[right]] = right
            result = max(result, right-left+1)

        return result       