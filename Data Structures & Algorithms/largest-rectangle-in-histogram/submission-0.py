class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        def pse(arr):
            stack = []
            res = [-1]*len(arr)

            for i in range(len(arr)):
                curr = arr[i]

                while stack and curr <= stack[-1][0]:
                    stack.pop()

                if stack:
                    res[i] = stack[-1][1]

                stack.append([curr, i])

            return res

        def nse(arr):
            stack = []
            res = [len(arr)]*len(arr)

            for i in range(len(arr)-1, -1, -1):
                curr = arr[i]

                while stack and curr <= stack[-1][0]:
                    stack.pop()

                if stack:
                    res[i] = stack[-1][1]

                stack.append([curr, i])

            return res

        pse_arr = pse(heights)
        nse_arr = nse(heights)
        
        maxA = 0

        for i in range(len(heights)):
            maxA = max(maxA, (nse_arr[i]-pse_arr[i]-1)*heights[i])

        return maxA

        
        