class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1

        if n == 1:
            return nums[0]

        while l <= r:
            if nums[l] <= nums[r]:
                return nums[l]

            mid = l + (r-l)//2
            prev = (mid+n-1)%n
            nxt = (mid+1)%n

            if nums[mid] <= nums[prev] and nums[mid] <= nums[nxt]:
                return nums[mid]
            elif nums[l] <= nums[mid]:
                l = mid+1
            else:
                r = mid-1



