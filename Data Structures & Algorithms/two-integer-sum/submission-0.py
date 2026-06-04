class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}

        for index, num in enumerate(nums):
            complement = target - num
            if complement in numbers:
                return [numbers[complement], index]
            numbers[num] = index

        return [-1,-1]