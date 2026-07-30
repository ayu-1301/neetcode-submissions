class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in my_dict:
                return [my_dict[dif], i]
            my_dict[nums[i]] = i
        return -1