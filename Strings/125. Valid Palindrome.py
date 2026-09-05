class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alphanum = ""
        for i in s:
            if i.isalnum():
                alphanum += i 
        if alphanum == alphanum[::-1]:
            return True
        else: 
            return False