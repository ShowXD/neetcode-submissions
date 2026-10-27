class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        result = False
        for num in nums:
            if num in count:
                result = True
                break
            count[num] = num
        return result