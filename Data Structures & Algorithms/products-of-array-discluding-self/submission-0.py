import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pp = 1
        ppl = [1]*n

        for i in range(1, n):
            pp = pp*nums[i-1]
            ppl[i] = pp

        sp = 1
        spl = [1]*n

        for j in range(n-2, -1, -1):
            sp = sp*nums[j+1]
            spl[j] = sp

        res = []
        for k in range(n):
            res.append(ppl[k]*spl[k])

        return res






        