class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if nums == []:
            return 0

        nums.sort()

        mxlen = 1
        curr_len = 1
        prev_ele = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != prev_ele and nums[i]== prev_ele+1:
                curr_len += 1
                mxlen = max(mxlen, curr_len)
                prev_ele = nums[i]
            elif nums[i] != prev_ele and nums[i] != prev_ele+1:
                curr_len = 1
                prev_ele = nums[i]
            elif nums[i] == prev_ele:
                continue

        return mxlen

            



        print(nums)

        return 1
        