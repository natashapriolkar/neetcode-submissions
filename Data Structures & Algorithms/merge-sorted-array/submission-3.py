class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1[m:] = nums2[:n]
        # nums1.sort()
        # This approach sorts the nums1 again at the end O((m + n) log (m + n))
        
        # Approach 2: Three pointers with extra space
        nums1_copy = nums1[:m]
        # Rebuild nums1 from beginning
        idx = 0    #for write position in nums1
        i = 0
        j = 0
        while idx < (m + n):
            if j >= n or (i < m and nums1_copy[i] <= nums2[j]):
                nums1[idx] = nums1_copy[i]
                i += 1

            else:
                nums1[idx] = nums2[j]
                j += 1

            idx += 1
