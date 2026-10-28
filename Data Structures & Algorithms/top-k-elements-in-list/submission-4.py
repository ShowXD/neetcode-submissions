class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        result = []

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        bucket = [[]for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            bucket[freq].append(num)

        for i in range(len(bucket)-1,-1,-1):
            result.extend(bucket[i])
            if len(result) >= k:
                return result

        return result