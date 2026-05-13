class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(ch for ch in s if ch.isalnum())
        i,j = 0, len(cleaned)-1
        while i<j:
            if cleaned[i].lower() != cleaned[j].lower():
                return False
            
            i= i+1
            j=j-1
        return True