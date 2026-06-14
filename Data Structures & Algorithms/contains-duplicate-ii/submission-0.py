class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        cond = False
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j] and abs(i - j) <= k:
                    print("J = " + str(j))
                    print("I = " + str(i))                    
                    cond = True
        return cond