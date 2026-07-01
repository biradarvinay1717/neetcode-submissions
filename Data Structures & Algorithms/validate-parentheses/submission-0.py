class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) < 2:
            return False
        d = {}
        stack = []


        for i in s:
            if i == '(': d[i] = ')'
            elif i == ')': d[i] = '('
            elif i == '[': d[i] = ']'
            elif i == ']': d[i] = '['
            elif i == '{': d[i] = '}'
            elif i == '}': d[i] = '{'

        i = 0
        for i in range(len(s)):
            curr = s[i]

            if curr in ['(', '{', '[']:
                stack.append(curr)
            else:
                if stack and d[curr] == stack[-1]:
                    stack.pop()
                else:
                    return False

        if stack:
            return False
        return True
        