class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dic = defaultdict(int)

        for n in nums:
            if n in dic:
                return True
            else:
                dic[n] =+ 1
        return False