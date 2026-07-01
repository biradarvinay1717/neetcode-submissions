class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        val = 0
        stack = []
        if len(tokens) == 1:
            return int(tokens[0])

        for i in range(len(tokens)):
            curr = tokens[i]

            if curr == '+':
                val = int(stack[-2]) + int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(val)

            elif curr == '-':
                val = int(stack[-2]) - int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(val)

            elif curr == '*':
                val = int(stack[-2]) * int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(val)
            
            elif curr == '/':
                val = int(stack[-2]) / int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(val)

            else:
                stack.append(int(curr))

        return int(stack[-1])
        