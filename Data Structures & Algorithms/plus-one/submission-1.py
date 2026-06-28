class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # txt = "".join(str(c) for c in digits)
        # num = int(txt)
        # num += 1
        # txt = str(num)
        # res = []
        # for c in txt:
        #     res.append(int(c))
        # return res
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        digits.insert(0, 1)
        return digits
        