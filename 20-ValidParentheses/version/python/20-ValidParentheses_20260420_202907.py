# Last updated: 4/20/2026, 8:29:07 PM
class Solution:
    def isValid(self, s: str) -> bool:
        invert_bracket = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if stack and stack[-1] == invert_bracket[c]:
                    stack.pop()
                else:
                    return False

        if stack:
            return False

        return True

        #     if c == ")" or c == "]" or c == "}":
        #         if stack[-1] != invert_bracket[c]:
        #             return False

        # return True















        # par_map = {")": "(", "}": "{", "]": "["}
        # open_set = {"(", "{", "["}

        # stack = []
        # for c in s:

        #     if c in open_set:
        #         stack.append(c)

        #     else:

        #         if not stack:
        #             return False

        #         e = stack.pop()
        #         if e != par_map[c]:
        #             return False

        # if stack:
        #     return False

        # return True
