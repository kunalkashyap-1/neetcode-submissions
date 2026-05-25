class Solution:
    def isValid(self, s: str) -> bool:
        bmap = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        stack = []
        for c in s:
            stack.append(c)
            if c in bmap and len(stack) > 1 and bmap[c] == stack[-2]:
                stack.pop()
                stack.pop()
        
        print(stack)
        # print(stack[-1])
        # print(bmap[c])
        return len(stack) == 0