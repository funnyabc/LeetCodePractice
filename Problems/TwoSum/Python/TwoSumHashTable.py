class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        hashset = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in hashset:
                return [i, nums.index(diff)]
            else:
                hashset[val] = i