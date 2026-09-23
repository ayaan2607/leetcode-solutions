class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check = set()
        for i in range(len(nums)):
            if nums[i] in check:
                return True
            elif nums[i] not in check:
                check.add(nums[i])
        return False