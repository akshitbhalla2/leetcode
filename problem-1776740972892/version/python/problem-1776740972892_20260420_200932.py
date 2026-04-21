# Last updated: 4/20/2026, 8:09:32 PM
1class Solution:
2    def calPoints(self, operations: List[str]) -> int:
3        
4        scores = []
5        for op in operations:
6            if op == "C":
7                scores.pop()
8            elif op == "D":
9                scores.append(scores[-1] * 2)
10            elif op == "+":
11                scores.append(scores[-1] + scores[-2])
12            else:
13                scores.append(int(op))
14        
15        return sum(scores)