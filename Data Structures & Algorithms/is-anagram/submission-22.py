class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        counter = [0] * 26

        for l in range(len(s)):
            counter[ord(s[l]) - ord('a')] += 1
            counter[ord(t[l]) - ord('a')] -= 1

        for v in counter:
            if v != 0:
                return False

        return True