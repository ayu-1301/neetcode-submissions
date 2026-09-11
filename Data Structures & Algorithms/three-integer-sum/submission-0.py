class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, v  in enumerate(nums):
            if v>0:
                break

            if i > 0 and v == nums[i-1]:
                continue
            
            left, right =  i + 1, len(nums) - 1

            while left < right:
                threeSum = v + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0: 
                    left += 1
                else: 
                    res.append([v,nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res

