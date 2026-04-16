class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = Counter(s)
        for char in t:
            count_s[char] -= 1

        for key, val in count_s.items():
            if val != 0:
                return False

        return True