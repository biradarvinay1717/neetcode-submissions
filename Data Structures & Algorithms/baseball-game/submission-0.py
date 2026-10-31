class Solution:
    def calPoints(self, operations: list[str]) -> int:

        st = []

        for i in range(len(operations)):

            ele = operations[i]

            if ele == "C":
                st.pop()
            elif ele == "D":
                st.append(2*st[-1])
            elif ele == "+":
                st.append(st[-1]+st[-2])
            else:
                st.append(int(ele))

        return sum(st)
        