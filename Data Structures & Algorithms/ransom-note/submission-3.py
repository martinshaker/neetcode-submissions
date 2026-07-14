class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = Counter(magazine)        

        for s in ransomNote:
            if s not in mag or mag[s] <= 0:
                return False
            else:
                mag[s] -= 1

        return True

        