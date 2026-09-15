class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        limit = len(nums)/3
        l = []

        for ele in d.keys():
            if d[ele] > limit:
                l.append(ele)

        return l