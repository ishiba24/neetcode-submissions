class Solution:
    def isPalindrome(self, s: str) -> bool:
       #how to determine if non ascii? 
        l, r= 0, len(s) - 1
        while l <= r:
            if self.alphanum(s[l]) == False:
                l += 1
                continue
            if self.alphanum(s[r])== False:
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
            
    def alphanum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'))