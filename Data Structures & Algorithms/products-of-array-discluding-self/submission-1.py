class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        product = 1
        for index, num in enumerate(nums):
            result[index] *= product
            product *= num
        product = 1
        for index in range(len(nums) - 1, - 1, - 1 ):
            result[index] *= product
            product *= nums[index]
        return result