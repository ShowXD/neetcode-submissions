class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = result = 0
        count = {}

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1

            if right - left + 1 - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            result = max(result, len(s[left:right+1]))

        return result