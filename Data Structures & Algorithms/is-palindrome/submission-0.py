class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_clean = ""
        for char in s:
            if char.isalnum() == False:
                continue
            s_clean += "".join(char)
        for index, char in enumerate(s_clean):
            left = index
            right = len(s_clean) - index - 1
            if s_clean[left] != s_clean[right]:
                return False
        return True