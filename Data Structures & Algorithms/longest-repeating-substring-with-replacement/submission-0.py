class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        fm = {}
        l,maxf,res = 0,0,0
        for r in range(len(s)):
            fm[s[r]] = fm.get(s[r],0) + 1
            maxf = max(maxf, fm[s[r]])
            if (r-l)+1-maxf > k:
                fm[s[l]] = fm[s[l]]-1
                l+=1
            res = r-l+1
        
        return res
                