class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = Counter(s)

        for c in t:
            count_s[c] -= 1

        for key, value in count_s.items():
            if value != 0:
                return False

        return True
        