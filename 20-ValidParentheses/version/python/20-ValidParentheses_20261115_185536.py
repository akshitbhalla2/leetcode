# Last updated: 11/15/2026, 6:55:36 PM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        # invert_bracket = {
4        #     ")": "(",
5        #     "]": "[",
6        #     "}": "{" 
7        # }
8        # stack = []
9        # for c in s:
10        #     if c == "(" or c == "[" or c == "{":
11        #         stack.append(c)
12        #     else:
13        #         if stack and stack[-1] == invert_bracket[c]:     
14        #             stack.pop()
15        #         else:
16        #             return False
17
18        # if stack:
19        #     return False
20
21        # return True
22
23        stack = []
24        pairs = {"}":"{", ")": "(", "]": "["}
25        for b in s:
26            if b == "{" or b == "(" or b == "[":
27                stack.append(b)
28            else:
29                if stack:
30                    if stack[-1] == pairs[b]:
31                        stack.pop()
32                    else:
33                        return False
34                else:
35                    return False
36        
37        if stack:
38            return False
39        
40        return True
41
42