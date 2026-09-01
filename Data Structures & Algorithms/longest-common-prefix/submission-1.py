class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        strs.sort()
        
        k = ""
        for i in range(len(strs[0])):
            if strs[0][i] == strs[-1][i]:
                k += strs[0][i]
            else:
                return k

        return k   