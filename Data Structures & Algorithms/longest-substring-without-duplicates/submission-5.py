class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prevMap = {}
        l = 0
        res = 0
        for r in range(len(s)):
            if s[r] in prevMap:
                l = max(l, 1 + prevMap[s[r]])

            prevMap[s[r]] = r
            res = max(res, r - l + 1)

        return res


        