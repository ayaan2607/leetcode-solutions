class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            n = nums[i]
            digit_sum = 0
            while n > 0:
                digit = n % 10
                digit_sum +=digit
                n //= 10
            if digit_sum == i:
                return i   
        return -1