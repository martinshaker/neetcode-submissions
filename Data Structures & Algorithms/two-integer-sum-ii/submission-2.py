class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sol = []
        for i in range(0,len(numbers)-1):
            for j in range(1,len(numbers)):

                print(numbers[i])
                if numbers[i] + numbers[j] == target:
                    sol.append(i+1)
                    sol.append(j+1) 
                    print(sol)
                    return sol