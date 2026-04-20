class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=l+1
        maxi = 0
        while r<len(prices):
            print("l",l)
            print("r",r)
            if prices[l] >= prices[r]:
                l = r
                if l+1 < len(prices):
                    r = l + 1
                    print("-- i am here --",l, r)
                else:
                    return maxi
            else:
                profit = prices[r] - prices[l]
                maxi = max(profit,maxi)
                r+=1

        return maxi


        
