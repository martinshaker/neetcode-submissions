class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(0,len(matrix)):
            print(matrix[i])
            if matrix[i][-1] >= target:
                print(matrix[i][-1])
                l, r = 0 , len(matrix[i])-1
                while l <= r:
                    m = (l+r)//2
                    if matrix[i][m] == target:
                        return True
                    elif matrix[i][m] > target:
                        r = m - 1
                    else:
                        l = m + 1
        return False
        
        