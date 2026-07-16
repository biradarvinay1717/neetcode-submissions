class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def func(nums, mid, days):
            d = 1
            sm = 0
            for i in range(len(nums)):
                if sm + nums[i] > mid:
                    d += 1
                    sm = nums[i]
                else:
                    sm += nums[i]
            return d <= days

        l, r = max(weights), sum(weights)

        ans = float("inf")

        while l <= r:
            mid = l + (r-l)//2
            res = func(weights, mid, days)
            if res:
                ans = min(ans, mid)
                r = mid-1
            else:
                l = mid+1
        return ans

