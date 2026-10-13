class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        if len(s) != len(t):
            return False

        counter_t = [0]*26
        counter_s = [0]*26

        for n in range(len(s)):
            counter_s[ord(s[n]) - ord('a')] += 1
            counter_t[ord(t[n]) - ord('a')] += 1

        if counter_t == counter_s:
            return True
        else:
            return False
        