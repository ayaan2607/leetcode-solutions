class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        merged = []
        for i in range(0,len(nums)-1,2):
            sum = int(str(nums[i]) + str(nums[i+1]))
            merged.append(sum)
        return min(merged)
        