# class Solution:
#     def majorityElement(self, nums: list[int]) -> list[int]:
#         d = {}
#         for num in nums:
#             d[num] = d.get(num, 0) + 1
        
#         limit = len(nums)/3
#         l = []

#         for ele in d.keys():
#             if d[ele] > limit:
#                 l.append(ele)

#         return l

from typing import List


class Solution:

    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        # Step 1: Candidate Selection
        cand1, cand2 = None, None
        count1, count2 = 0, 0

        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
            elif count1 == 0:
                cand1, count1 = num, 1
            elif count2 == 0:
                cand2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        # Step 2: Verification
        result = []
        threshold = len(nums) // 3

        for cand in (cand1, cand2):
            if cand is not None and nums.count(cand) > threshold:
                result.append(cand)

        return result