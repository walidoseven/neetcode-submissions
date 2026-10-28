class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        stocker = defaultdict(int)

        for i,n in enumerate(nums):

            difference = target - n

            if difference in stocker:
                return [stocker[difference], i]

            stocker[n] = i