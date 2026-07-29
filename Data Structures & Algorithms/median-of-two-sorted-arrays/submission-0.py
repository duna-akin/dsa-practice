class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedArray = nums1 + nums2
        mergedArray.sort()
        length = len(mergedArray)
        if length % 2 == 0:
            return (mergedArray[length // 2 - 1] + mergedArray[length // 2]) / 2
        else:
            return mergedArray[length // 2]