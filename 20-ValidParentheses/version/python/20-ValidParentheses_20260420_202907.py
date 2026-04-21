# Last updated: 4/20/2026, 8:29:07 PM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        invert_bracket = {
4            ")": "(",
5            "]": "[",
6            "}": "{" 
7        }
8        stack = []
9        for c in s:
10            if c == "(" or c == "[" or c == "{":
11                stack.append(c)
12            else:
13                if stack and stack[-1] == invert_bracket[c]:     
14                    stack.pop()
15                else:
16                    return False
17
18        if stack:
19            return False
20
21        return True
22
23        #     if c == ")" or c == "]" or c == "}":
24        #         if stack[-1] != invert_bracket[c]:
25        #             return False 
26        
27        # return True
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43        # par_map = {")": "(", "}": "{", "]": "["}
44        # open_set = {"(", "{", "["}
45
46        # stack = []
47        # for c in s:
48            
49        #     if c in open_set:
50        #         stack.append(c)
51            
52        #     else:
53                
54        #         if not stack:
55        #             return False
56                
57        #         e = stack.pop()
58        #         if e != par_map[c]:
59        #             return False
60
61        # if stack:
62        #     return False
63
64        # return True
65            
66
67