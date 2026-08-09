class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n1 = sorted(s)
        n2 = sorted(t)

        if n1 == n2:
            return True
        return False

        