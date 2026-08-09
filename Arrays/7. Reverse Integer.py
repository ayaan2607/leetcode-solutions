class Solution:
    def reverse(self, x: int) -> int:
        length = len(str(abs(x)))
        num = abs(x)
        reverse = 0

        for i in range(length):
            digit = num % 10
            reverse = reverse * 10 + digit
            num = num // 10

        if x < 0:
            reverse = -reverse

        if reverse < -2147483648 or reverse > 2147483647:
            return 0

        return reverse