class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # result = defaultdict(list)
        # for s in strs:
        #     sortedS = "".join(sorted(s))
        #     result[sortedS].append(s)

        # return list(result.values())

        result = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            result[tuple(count)].append(s)

        return list(result.values())
        