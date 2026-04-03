class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        maxprice = 0
        while r<len(prices):
            price = prices[r]-prices[l]
            if prices[l]< prices[r]:
                maxprice = max(maxprice,price)
            else:
                l=r
            r+=1
        return maxprice
