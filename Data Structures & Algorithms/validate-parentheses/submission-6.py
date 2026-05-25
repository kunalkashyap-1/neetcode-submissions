class Solution:
    def isValid(self, s: str) -> bool:
        bmap = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        stack = []
        for c in s:
            if c in bmap:
                if stack and stack[-1] == bmap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0