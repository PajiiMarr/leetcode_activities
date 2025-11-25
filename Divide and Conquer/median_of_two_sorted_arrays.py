from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always binary search the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left_total = (m + n + 1) // 2
        
        l, r = 0, m
        
        while l <= r:
            i = (l + r) // 2  # partition in nums1
            j = left_total - i  # partition in nums2
            
            # Edge values
            A_left  = nums1[i-1] if i > 0 else float('-inf')
            A_right = nums1[i]   if i < m else float('inf')
            B_left  = nums2[j-1] if j > 0 else float('-inf')
            B_right = nums2[j]   if j < n else float('inf')
            
            # Correct partition
            if A_left <= B_right and B_left <= A_right:
                # Odd total length → max of left
                if (m+n) % 2 == 1:
                    return max(A_left, B_left)
                # Even total → average of middle two
                return (max(A_left, B_left) + min(A_right, B_right)) / 2
            
            elif A_left > B_right:
                r = i - 1
            else:
                l = i + 1

if __name__ == "__main__":
    s = Solution()

    print(s.findMedianSortedArrays([1, 3], [2])) 

    print(s.findMedianSortedArrays([1, 2], [3, 4]))

    # Additional tests
    print(s.findMedianSortedArrays([], [1]))
    print(s.findMedianSortedArrays([0, 0], [0, 0]))