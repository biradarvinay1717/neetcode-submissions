class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0
        minL = float("inf")
        summ = 0

        for r in range(len(nums)):
            summ += nums[r]

            while summ >= target:
                minL = min(minL, r-l+1)
                summ -= nums[l]
                l += 1

        if minL == float("inf"):
            return 0
        return minL