class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        result = r
        while l <= r:
            totalTime = 0
            k = l + (r - l) // 2
            for p in piles:
                totalTime += math.ceil(float(p)/k)

            if totalTime <= h:
                result = k
                r = k - 1
            else:
                l = k + 1

        return result