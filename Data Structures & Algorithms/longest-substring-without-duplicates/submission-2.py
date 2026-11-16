class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = left = right = 0
        seen = set()
        while right < len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            right += 1
            longest = max(longest, len(seen))
        return longest