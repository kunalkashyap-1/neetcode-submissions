class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sl = 0
        sub = ""
        l,r = 0,1
        if len(s) == 1:
            return 1
        while r < len(s):
            sub = s[l:r]
            if s[r] not in sub:
                r+=1
                sub = s[l:r]
                sl = max(sl, len(sub))
            else:
                l += 1
        
        return sl