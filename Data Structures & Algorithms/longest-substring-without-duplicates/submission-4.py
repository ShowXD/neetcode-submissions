class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = longest = 0
        mask = 0

        for right, char in enumerate(s):  # 遍歷字串對應的 bit
            bit = 1 << (ord(char) - 32)
            
            while mask & bit:  # 如果遍歷到的字元已經看過
                left_bit = 1 << (ord(s[left]) - 32)
                mask -= left_bit
                left += 1

            mask += bit
            longest = max(longest, right - left + 1)
        return longest
