class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        word_stocker = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for w in s:
                count[ord(w) - ord('a')] += 1
            
            word_stocker[tuple(count)].append(s)
        return list(word_stocker.values())




                

                