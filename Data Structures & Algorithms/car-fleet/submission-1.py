class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = []
        stack = []

        for i in range(n):
            cars.append((position[i], (target - position[i])/speed[i]))

        cars.sort()
        for i in range(n-1, -1, -1):

            curr = cars[i]

            if not stack or curr[1] > stack[-1]:
                stack.append(curr[1])


        return len(stack)