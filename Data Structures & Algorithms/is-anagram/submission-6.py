class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen=set()
        seen.add(tuple(sorted(s)))
        if tuple(sorted(t)) in seen:
            return True
        return False