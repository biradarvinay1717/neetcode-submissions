class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        cheapest = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            cheapest = min(cheapest, prices[i])
            profit = max(profit, prices[i]-cheapest)
        
        return profit
        
        # max_p = 0

        # res = []

        # for i in range(len(prices)-1):
        #     curr_p = max(prices[i+1:]) - prices[i]
        #     max_p = max(curr_p, max_p)

        # return max_p
        