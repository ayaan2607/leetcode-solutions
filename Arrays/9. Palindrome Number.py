class Solution:
    def isPalindrome(self, x: int) -> bool:
        length = len(str(x))
        reverse = 0
        num = x
        for i in range(length):
            digit = num % 10
            reverse = reverse * 10 + digit
            num = num // 10

        if int(x) == int(reverse):
            return True
        else:
            return False