
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = longest = 0
        last_seen = [-1] * 128

        for right, char in enumerate(s):
            index = ord(char)
            previous = last_seen[index]

            left = max(left, previous + 1)
            last_seen[index] = right
            longest = max(longest, right - left + 1)

        return longest
