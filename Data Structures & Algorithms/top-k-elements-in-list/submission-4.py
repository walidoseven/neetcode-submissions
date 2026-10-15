class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = defaultdict(int)

        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            counter[n] += 1
        for n, cnt in counter.items():
            freq[cnt].append(n)
        
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
