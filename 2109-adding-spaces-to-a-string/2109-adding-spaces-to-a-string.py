class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        box = []
        i = 0
        for j in spaces:
            box.append(s[i:j])
            i = j
            box.append(" ")
        box.append(s[spaces[-1]:])
        return "".join(box)
