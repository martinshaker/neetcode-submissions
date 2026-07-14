class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t:
            return True

        ps, pt = 0,0

        while ps < len(s) and pt < len(t):
            if s[ps] == t[pt]:
                ps += 1
                pt += 1
            else:
                pt += 1

        return ps == len(s)


        