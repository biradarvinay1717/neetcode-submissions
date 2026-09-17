class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i, j, k = 0, 0, 0
        arr = [0]*(m+n)

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                arr[k] = nums1[i]
                i += 1
                k += 1
            elif nums1[i] >= nums2[j]:
                arr[k] = nums2[j]
                j += 1
                k += 1
        
        while i < m:
            arr[k] = nums1[i]
            i += 1
            k += 1

        while j < n:
            arr[k] = nums2[j]
            j += 1
            k += 1

        for c in range(m+n):
            nums1[c] = arr[c]
