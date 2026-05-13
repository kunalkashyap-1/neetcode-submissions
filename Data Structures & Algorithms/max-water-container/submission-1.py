class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i,j = 0, len(heights)-1
        res = 0
        while i < j:
            water = (j-i) * min(heights[i], heights[j])
            res = max(res, water)
            
            if heights[i] > heights[j]:
                j-=1
            else:
                i+=1
        
        return res