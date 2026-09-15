class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in range(len(nums2)):
            nums1.append(nums2[i])

        nums1.sort()

        n = len(nums1)
        mid = n//2
        
        if n % 2 != 0:
            return float(nums1[mid])
        else:
            return float((nums1[mid-1] + nums1[mid]) / 2.0)