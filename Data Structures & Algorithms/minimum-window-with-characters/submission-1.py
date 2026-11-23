from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        need = Counter(t)
        required = len(need)          # 需達標的字元種類數
        window = Counter()
        formed = 0                    # 已達標的種類數
        best = (float("inf"), 0, 0)   # (長度, 左界, 右界)

        left = 0
        for right, ch in enumerate(s):
            window[ch] += 1
            if ch in need and window[ch] == need[ch]:
                formed += 1

            while formed == required:             # 窗口合法 → try 收縮
                if right - left + 1 < best[0]:
                    best = (right - left + 1, left, right)
                lch = s[left]
                window[lch] -= 1
                if lch in need and window[lch] < need[lch]:
                    formed -= 1
                left += 1

        return "" if best[0] == float("inf") else s[best[1]:best[2] + 1]