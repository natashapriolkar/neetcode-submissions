class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indexMap = {}
        left = 0
        result = 0
        for right in range(len(s)):
            if s[right] in indexMap:
                left = max(left, indexMap[s[right]] + 1)

            indexMap[s[right]] = right
            result = max(result, right - left + 1)

        return result