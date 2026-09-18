class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        element_sum = 0
        digit_sum = 0
        digit = []
        for i in range(len(nums)):
            element_sum = element_sum + nums[i]
        
        for j in range(len(nums)):
            while nums[j] > 0:
                digit.append(nums[j] % 10)
                nums[j] //= 10
        
        for k in range(len(digit)):
            digit_sum = digit_sum + digit[k]
        
        return abs(element_sum - digit_sum)
