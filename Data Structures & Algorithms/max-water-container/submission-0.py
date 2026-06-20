class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximumArea = 0
        area = 0

        for i in range(len(heights)):
            for j in range(1,len(heights)):
                area = (j-i)*min(heights[i],heights[j])
                if area > maximumArea:
                    maximumArea = area

        return maximumArea
