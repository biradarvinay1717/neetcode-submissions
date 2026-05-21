class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = {}

        for i in range(len(strs)):
            k = "".join(sorted(strs[i][::-1]))

            if k not in d:
                d[k] = [strs[i]]
            else:
                d[k].append(strs[i])

        m = []
        for j in d.values():
            m.append(j)

        return m