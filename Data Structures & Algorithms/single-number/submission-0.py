class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums.count(int(nums[i])) == 1:
                return int(nums[i])
        