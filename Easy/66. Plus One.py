class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        result = 0
        digit = []
        for i in digits:
            result = result * 10 + i
        result = result + 1
        while result > 0:
            digit.append(result % 10)
            result //= 10
        digit.reverse()
        return digit

