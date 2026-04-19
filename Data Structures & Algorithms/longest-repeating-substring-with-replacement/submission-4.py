class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxFreq = 0
        res = 0
        count = {}  # Frequency map for string s
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxFreq = max(maxFreq, count[s[r]])

            while (r - l + 1) - maxFreq > k:
                #shrink window size
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res





                



        