# Last updated: 11/15/2026, 6:01:47 PM
class Solution:
    def calPoints(self, operations: List[str]) -> int:

        # scores = []
        # for op in operations:
        #     if op == "C":
        #         scores.pop()
        #     elif op == "D":
        #         scores.append(scores[-1] * 2)
        #     elif op == "+":
        #         scores.append(scores[-1] + scores[-2])
        #     else:
        #         scores.append(int(op))

        # return sum(scores)

        scores = []
        for op in operations:
            if op == "+":
                scores.append(scores[-1] + scores[-2])
            elif op == "D":
                scores.append(2*scores[-1])
            elif op == "C":
                scores.pop()
            else:
                scores.append(int(op))
        return sum(scores)
