class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        for ch in s:
            map[ch] = map.get(ch,0) + 1
        
        for ch in t:
            if ch not in map.keys():
                return False
            map[ch] = map.get(ch,1) - 1
        
        for value in map.values():
            if value != 0:
                return False
        
        return True

            