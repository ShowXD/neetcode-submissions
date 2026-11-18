class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = result = 0
        count = {}

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(count.values())
            windows_length = right - left + 1

            if windows_length - max_freq > k:  # 當視窗長度內需要替換的字母數量已經大於K則移動left使視窗縮小
                count[s[left]] -= 1
                left += 1

            result = max(result, len(s[left:right+1]))

        return result