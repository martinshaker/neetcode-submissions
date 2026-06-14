class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortedS = list(s)
        sortedS.sort()
        sortedT = list(t)
        sortedT.sort()

        if sortedS != sortedT:
            return False
        return True

        for i in range(0,len(sortedS)):
            if sortedS[i] != sortedT[i]:
                return False
        return True