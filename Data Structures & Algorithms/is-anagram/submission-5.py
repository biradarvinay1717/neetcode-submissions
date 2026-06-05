class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # d = {}
        # k = {}

        # for i in range(len(s)):
        #     if s[i] not in d:
        #         d[s[i]] = 1
        #     else:
        #         d[s[i]] += 1

        # for j in range(len(t)):
        #     if t[j] not in k:
        #         k[t[j]] = 1
        #     else:
        #         k[t[j]] += 1
                
        # if d == k:
        #     return True
        # return False

        d = {}

        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0) + 1

        for j in range(len(t)):
            if t[j] not in d:
                return False
            else:
                d[t[j]] -= 1
                if d[t[j]] < 0:
                    return False

        return sum(d.values()) == 0















