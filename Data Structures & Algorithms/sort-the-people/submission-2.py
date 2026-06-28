class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        paired = list(zip(names, heights))
        res = []
        paired.sort(key = lambda x: x[1], reverse = True)
        for name, h in paired:
            res.append(name)
        return res
