class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        result = defaultdict(list)

        for s in strs:
            counter = [0] * 26
            for l in s:
                counter[ord(l) - ord('a')] += 1
            
            result[tuple(counter)].append(s)
        return list(result.values())


