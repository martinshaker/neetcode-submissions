class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest = 0
        highList = []

        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j]>prices[i]:
                    highest = prices[j]-prices[i]
                    highList.append(highest)
                    print(highList)
        if not highList:
            return highest
        return max(highList)



                




        