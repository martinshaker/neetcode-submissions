class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1
        index_m = m-1
        index_n = n-1

        while index_m >= 0 and index_n >= 0:
            if nums1[index_m] > nums2[index_n]:
                nums1[last] = nums1[index_m]
                print(nums1)
                index_m -= 1
            else:
                nums1[last] = nums2[index_n]
                print(nums1)
                index_n -= 1
            last -= 1

        while index_n >= 0:
            nums1[last] = nums2[index_n]
            index_n -= 1
            last -= 1

        return nums1