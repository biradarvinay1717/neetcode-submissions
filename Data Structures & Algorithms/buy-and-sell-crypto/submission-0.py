class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_p = 0

        res = []

        for i in range(len(prices)-1):
            curr_p = max(prices[i+1:]) - prices[i]
            max_p = max(curr_p, max_p)

        return max_p
        