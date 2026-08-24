class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        result = []

        for a, n in enumerate(nums):

            if a>0 and nums[a] == nums[a-1]:
                continue


            i = a + 1
            k = len(nums) - 1


            while i<k:
                if i > a+1 and nums[i] == nums[i-1]:
                    i += 1
                    continue

                Sum = nums[a] + nums[i] + nums[k]

                if Sum > 0:
                    k -= 1

                elif Sum < 0:
                    i += 1
                
                else:
                    result.append([nums[a], nums[i], nums[k]])
                    i += 1
                    k -= 1
        return result



                    

                
                

                
 
            

            




            
            




            