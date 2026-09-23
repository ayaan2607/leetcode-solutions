class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums) + 1
        count = 0
        sum = length*(length - 1) / 2
        for i in nums:
            count += i
        num = int(sum - count)
        return num