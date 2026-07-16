class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        reversed_str = s[::-1]
        if reversed_str == s:
            return True
        return False