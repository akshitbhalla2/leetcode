# Last updated: 11/15/2026, 6:01:47 PM
1class Solution:
2    def calPoints(self, operations: List[str]) -> int:
3        
4        # scores = []
5        # for op in operations:
6        #     if op == "C":
7        #         scores.pop()
8        #     elif op == "D":
9        #         scores.append(scores[-1] * 2)
10        #     elif op == "+":
11        #         scores.append(scores[-1] + scores[-2])
12        #     else:
13        #         scores.append(int(op))
14        
15        # return sum(scores)
16
17        scores = []
18        for op in operations:
19            if op == "+":
20                scores.append(scores[-1] + scores[-2])
21            elif op == "D":
22                scores.append(2*scores[-1])
23            elif op == "C":
24                scores.pop()
25            else:
26                scores.append(int(op))
27        return sum(scores)