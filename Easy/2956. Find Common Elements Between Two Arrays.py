class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        one = 0
        two = 0
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                one+=1
        for j in range(len(nums2)):
            if nums2[j] in nums1:
                two+=1
        output.append(one)
        output.append(two)
        return output