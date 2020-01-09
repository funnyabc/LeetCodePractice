class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        for i in range(len(nums)):
            find_number = target - nums[i]
            if find_number in nums and i != nums.index(find_number):
                return [i, nums.index(find_number)]