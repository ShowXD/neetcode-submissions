
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        target = {}
        now_window = {}

        for char in t:
            target[char] = target.get(char, 0) + 1

        required = len(target)
        formed = 0

        left = 0
        best_left = 0
        best_length = float("inf")

        for right in range(len(s)):
            char = s[right]
            now_window[char] = now_window.get(char, 0) + 1

            if char in target and now_window[char] == target[char]:
                formed += 1

            while formed == required:
                window_length = right - left + 1

                if window_length < best_length:
                    best_length = window_length
                    best_left = left

                left_char = s[left]
                now_window[left_char] -= 1

                if left_char in target and now_window[left_char] < target[left_char]:
                    formed -= 1

                left += 1

        if best_length == float("inf"):
            return ""

        return s[best_left:best_left + best_length]
