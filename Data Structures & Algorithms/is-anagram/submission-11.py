class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        counter_s = [0]*26
        counter_t = [0]*26

        for l in range(len(s)):
            counter_s[ord(s[l]) - ord('a')] += 1
            counter_t[ord(t[l]) - ord('a')] += 1
        
        if counter_s == counter_t:
            return True
        else:
            return False