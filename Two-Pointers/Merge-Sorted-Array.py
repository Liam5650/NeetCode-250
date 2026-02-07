from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        # Use pointers to show where we are in each array
        p1 = m - 1
        p2 = n - 1

        # Rebuild the first array from the back, taking use of the empty
        # space. Careful indexing means we will only overwrite already
        # processed values of the trailing 0s
        for i in range(len(nums1) - 1, -1, -1):
            
            if p1 >= 0 and p2 < 0:
                nums1[i] = nums1[p1]
                p1 -= 1

            elif p1 < 0 and p2 >= 0:
                nums1[i] = nums2[p2]
                p2 -= 1

            elif nums1[p1] > nums2[p2]:
                nums1[i] = nums1[p1]
                p1 -= 1

            elif nums1[p1] <= nums2[p2]:
                nums1[i] = nums2[p2]
                p2 -= 1