class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []

        for s in strs:
            res.append(f"{len(s)}#{s}")

        return "".join(res)

    def decode(self, s: str) -> List[str]:

        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            lenght = int(s[i:j])
            i = j + 1

            word = s[i:i + lenght]
            res.append(word)

            i += lenght
        return res

# encode -> 4#leet4#code