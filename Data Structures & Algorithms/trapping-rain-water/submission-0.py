class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        p = [0] * n
        p[0] = height[0]

        for i in range(1, n):
            p[i] = max(p[i - 1], height[i])
        
        s = [0] * n
        s[n - 1] = height[n - 1]

        for i in range(n - 2, -1, -1):
            s[i] = max(height[i], s[i + 1])
        
        res = 0
        for i in range(n):
            res += min(p[i], s[i]) - height[i]
        
        return res