class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l < r:
            if nums[r-1] < nums[r]:
                r -= 1

            else:
                return min(nums[r],nums[r-1])

        return min(nums[l],nums[r])