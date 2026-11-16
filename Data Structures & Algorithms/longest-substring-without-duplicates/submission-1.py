class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        seen = set()
        longest = 0
        while right != len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            else:
                seen.add(s[right])
            right += 1
            longest = max(longest, len(seen))
        return longest