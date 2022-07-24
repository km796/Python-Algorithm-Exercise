from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        small = nums1 if len(nums1) <= len(nums2) else nums2
        big = nums1 if len(nums1) > len(nums2) else nums2
        tot = len(small) + len(big)
        isEven = tot%2 == 0

        start = 0
        end = len(small)
        while True:
            x = start + (end-start)//2
            y = tot//2 - x

            maxX = small[x-1] if x-1>=0 else float('-inf')
            maxY = big[y-1] if y-1>=0 else float('-inf')

            minXb = small[x] if x<len(small) else float('inf')
            minYb = big[y] if y<len(big) else float('inf')

            if maxX <= minYb and maxY <= minXb:
                ans = (max(maxX, maxY) + min(minXb, minYb))/2 if isEven else min(minYb, minXb)
                return ans
            elif maxX > minYb:
                end = x
            elif maxY > minXb:
                start = x if x != len(small)-1 else x+1

sol = Solution()
print(sol.findMedianSortedArrays([1,3], [2, 7]))


