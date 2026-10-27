class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first = []
        last = []
        output = []
        for i in range(n):
            first.append(nums[i])
        for j in range(n,2*n):
            last.append(nums[j])
        for k in range(n):
            output.append(first[k])
            output.append(last[k])
        
        return output
        