class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #at each point you can choose to add an opening or a closing, but your limit for each is n
        #opening can never be the last
        opening = n
        closing = n
        res = []
        curString = []
        def backtrack(opening, closing, curString):
            if opening == 0 and closing == 0:
                res.append("".join(curString))
                return
            if opening >= 1 and opening <= closing:
                curString.append('(')
                backtrack(opening - 1, closing, curString)
                curString.pop()
            if closing >= 1:
                curString.append(')')
                backtrack(opening, closing - 1, curString)
                curString.pop()
        backtrack(opening, closing, curString)
        return res
