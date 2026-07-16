from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # if len(piles) == 1:
        #     return ceil(piles[0]/h)
        
        def func(nums, mid, h):
            hrs = 0
            for i in range(len(nums)):
                hrs += ceil(nums[i]/mid)
            if hrs > h:
                return False
            return True


        l, r = 1, max(piles)

        ans = float("inf")

        while l <= r:
            mid = l + (r-l)//2
            res = func(piles, mid, h)
            if res:
                ans = min(ans, mid)
                r = mid-1
            else:
                l = mid+1

        return ans





