class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            test = nums.copy()
            value = test[i]
            del test[i]
            if value not in test:
                return value
