class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        prefix = 1
        for i in range(n):
            res[i] = prefix # res = [1,1,2,8]
            prefix *= nums[i] #nums = [1,2,4,6]

        suffix = 1
        for i in range(n -1, -1, -1):
            res[i] *= suffix # res = [1,1,2,8]
            suffix *= nums[i] #nums = [1,2,4,6]

        return res