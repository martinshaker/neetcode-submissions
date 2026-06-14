class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            m = l + ((r - l) // 2)  
            print("m= {}".format(m))
            if nums[m] >= target:
                r = m
                print("r= {}".format(r))
            elif nums[m] < target:
                l = m + 1
                print("l= {}".format(l))
        return l if (l < len(nums) and nums[l] == target) else -1
        