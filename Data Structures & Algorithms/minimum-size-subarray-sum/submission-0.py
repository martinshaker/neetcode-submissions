class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0

        l, total = 0, 0
        best = float("inf")

        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                best = min(best,r-l+1)
                total -= nums[l]
                l += 1

        return best



        