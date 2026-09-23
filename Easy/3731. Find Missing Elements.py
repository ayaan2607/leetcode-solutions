class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        sorted_list = sorted(nums)
        missing = []
        for i in range(sorted_list[0],sorted_list[-1]):
            if i not in sorted_list:
                missing.append(i)
        return missing