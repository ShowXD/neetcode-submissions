class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        seen = set(nums)
        for num in seen:
            if num - 1 not in seen:
                count = 1
                while num + 1 in seen:
                    num += 1
                    count += 1
                longest = max(longest, count)
        return longest