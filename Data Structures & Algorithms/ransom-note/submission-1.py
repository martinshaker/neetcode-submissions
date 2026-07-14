class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = {}        

        for i in magazine:
            mag[i] = magazine.count(i)

        for s in ransomNote:
            if s not in mag or mag[s] <= 0:
                return False
            else:
                mag[s] -= 1

        if mag:
            return True

        