class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #use freq count arrays, if at any point they match, then we return True
        if len(s1) > len(s2):
            return False
        
        freq1 = [0] * 26
        freq2 = [0] * 26
        for i in range(len(s1)):
            freq1[ord(s1[i]) - ord('a')] += 1
            freq2[ord(s2[i]) - ord('a')] += 1
        matches = 0
        for i in range(26):
            matches += (1 if freq1[i] == freq2[i] else 0)
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26 :
                return True
            index = ord(s2[r]) - ord('a')
            freq2[index] += 1
            if freq1[index] == freq2[index]:
                matches += 1
            elif freq1[index] +1 == freq2[index]:
                matches -= 1
            index2 = ord(s2[l]) - ord('a')
            freq2[index2] -= 1
            if freq1[index2] == freq2[index2]:
                matches += 1
            elif freq1[index2] - 1 == freq2[index2]:
                matches -= 1
            l += 1
        return matches == 26
        
