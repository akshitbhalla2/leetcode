# Last updated: 11/15/2026, 6:55:36 PM
class Solution:
    def isValid(self, s: str) -> bool:
        # invert_bracket = {
        #     ")": "(",
        #     "]": "[",
        #     "}": "{"
        # }
        # stack = []
        # for c in s:
        #     if c == "(" or c == "[" or c == "{":
        #         stack.append(c)
        #     else:
        #         if stack and stack[-1] == invert_bracket[c]:
        #             stack.pop()
        #         else:
        #             return False

        # if stack:
        #     return False

        # return True

        stack = []
        pairs = {"}":"{", ")": "(", "]": "["}
        for b in s:
            if b == "{" or b == "(" or b == "[":
                stack.append(b)
            else:
                if stack:
                    if stack[-1] == pairs[b]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False

        if stack:
            return False

        return True
