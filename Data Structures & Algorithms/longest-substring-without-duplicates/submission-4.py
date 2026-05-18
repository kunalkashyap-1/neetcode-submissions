class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sl = 0
        l,r = 0,1
        if len(s) == 1:
            return 1
        while r < len(s):
            if s[r] not in s[l:r]:
                r+=1
                sl = max(sl, len(s[l:r]))
            else:
                l += 1
        
        return sl