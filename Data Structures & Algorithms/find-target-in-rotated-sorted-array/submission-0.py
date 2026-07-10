class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def func(nums, n):
            l, r = 0, n-1
            while l <= r:
                if nums[l] <= nums[r]:
                    return l

                mid = l + (r-l)//2
                prev = (mid+n-1)%n
                nxt = (mid+1)%n

                if nums[mid] <= nums[prev] and nums[mid] <= nums[nxt]:
                    return mid
                elif nums[l] <= nums[mid]:
                    l = mid+1
                else:
                    r = mid-1

        mid = func(nums, len(nums))

        def bs(nums, l, r, ele):
            while l <= r:
                mid = l + (r-l)//2

                if ele == nums[mid]:
                    return mid
                elif ele < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1

            return -1

        a = bs(nums, 0, mid, target)
        b = bs(nums, mid, len(nums)-1, target)

        return max(a, b)
        






