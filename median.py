class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = sorted(nums1 + nums2)

        numOfEls = len(nums3)
        if numOfEls % 2 == 0:
        	halfPointLeft, halfPointRight = int(numOfEls/2), int(numOfEls/2)+1
        	return (nums3[halfPointLeft]+nums3[halfPointRight])/2
        else:
        	return nums3[int(numOfEls/2)]



sol = Solution()
print sol.findMedianSortedArrays([7,1],[2,3])