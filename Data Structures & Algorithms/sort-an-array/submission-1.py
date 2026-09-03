class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        OFFSET, RANGE = 50000, 100001

        count = [0]*RANGE
        for num in nums:
            count[num + OFFSET] += 1

        idx = 0
        for i in range(RANGE):
            while count[i] > 0:
                nums[idx] = i - OFFSET
                idx += 1
                count[i] -= 1

        return nums