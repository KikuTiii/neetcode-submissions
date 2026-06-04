class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vistos= {}

        for num in nums:
            if num in vistos:
                return True
            vistos[num] = True
        return False