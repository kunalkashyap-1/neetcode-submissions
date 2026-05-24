class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 1
        tcount = {}
        window = {}

        if len(t) > len(s): return ""
        if len(t) == 0: return ""

        for ch in t:
            tcount[ch] = tcount.get(ch,0) + 1
        
        have, need = 0, len(tcount)
        res, reslen = [-1,-1], float("infinity")
        l=0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c,0) +1

            if c in tcount and window[c] == tcount[c]:
                have += 1
            
            while have == need:
                if (r-l+1) < reslen:
                    res = [l,r]
                    reslen = r-l+1
                
                window[s[l]] -=1
                if s[l] in tcount and window[s[l]] < tcount[s[l]]:
                    have -= 1

                l+=1
        
        l,r = res

        return s[l:r+1] if reslen != float("infinity") else ""