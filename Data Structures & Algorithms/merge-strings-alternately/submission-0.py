class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        if len(word1) > len(word2):
            n = len(word2)
        else:
            n = len(word1)

        k = ""
        for i in range(n):
            k += word1[i]
            k += word2[i]

        k += word1[n:]
        k += word2[n:]
        return k
        