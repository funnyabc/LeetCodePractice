class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        if len(nums) == 2:
            return [0, 1]
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                j += 1
            i += 1