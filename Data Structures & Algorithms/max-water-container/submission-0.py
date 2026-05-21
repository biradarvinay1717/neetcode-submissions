class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l, r = 0, len(heights)-1
        a = 0

        while l <r:
            area = (r-l)*min(heights[l], heights[r])
            a = max(a, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return a
        