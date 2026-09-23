class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        output = len(nums)
        for i in nums[:]:
            if i == val:
                nums.remove(val)
                output -= 1
        
        return output
            
        