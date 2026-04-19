class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        prevMap = {}
        res = 0
        for r in range(len(s)):
            if s[r] in prevMap:
                l = max(l, prevMap[s[r]] + 1)

            
            prevMap[s[r]] = r
            res = max(res, r - l + 1)

        return res


        