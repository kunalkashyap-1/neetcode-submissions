class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join([ch for ch in s if ch.isalnum()])
        cleaned = cleaned.lower()
        return cleaned == cleaned[::-1]