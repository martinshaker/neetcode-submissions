class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''

        if not strs:
            return ""
        for s in strs:
            encoded = encoded + s + '~'
            print (encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        if s.strip() == "":
            return [""]
        decoded = s.split('~')
        return decoded[:-1]


            
