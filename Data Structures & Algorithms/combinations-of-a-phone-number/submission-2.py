class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #keep track of each digit, and iterate through each digits possibility. at each point, explore that digit and then pop it when returned, explore the next
        #prolly do for dig in dToC[num]
        if not digits:
            return []
        res = []
        dToC = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"}
        curString = []
        def backtrack(i):
            if i >= len(digits):
                res.append("".join(curString))
                return
            num = digits[i]
            for dig in dToC[num]:
                curString.append(dig)
                backtrack(i + 1)
                curString.pop()
        backtrack(0)
        return res