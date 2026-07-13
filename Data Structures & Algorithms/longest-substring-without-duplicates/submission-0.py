class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        charSet = set()

        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[l])
                print('removed', charSet)
                l += 1
                print('l= ', l)
            charSet.add(s[i])
            print('added', charSet)
            longest = max(longest, i - l + 1)
            print('max longest', longest)

        return longest

        

        

        