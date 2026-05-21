class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        count_1 = [0]*26
        count_2 = [0]*26
        k = len(s1)

        for i in range(k):
            count_1[ord(s1[i]) - ord('a')] += 1
            count_2[ord(s2[i]) - ord('a')] += 1

        for i in range(k, len(s2)):
            if count_1 == count_2:
                return True

            count_2[ord(s2[i]) - ord('a')] += 1
            count_2[ord(s2[i-k]) - ord('a')] -= 1

        return count_1 == count_2
        