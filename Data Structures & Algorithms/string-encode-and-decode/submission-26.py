class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + '#' + s
        return encoded

    def decode(self, s: str) -> List[str]:
        l,r = 0,0
        decoded = []
        while r < len(s):
            while s[r] != '#':
                r += 1
            length = int(s[l:r])
            decoded.append(s[r+1:r+1+length])
            l = r+1+length
            r = l
        return decoded
