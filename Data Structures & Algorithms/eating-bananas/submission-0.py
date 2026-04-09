class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(p for p in piles)
        
        while l<=r:
            mid = (l+r)//2
            sum = 0
            for p in piles:
                sum += math.ceil(p/mid)
            if sum <=h:
                res = mid
                r = mid-1
            else:
                l = mid+1
        return res
            