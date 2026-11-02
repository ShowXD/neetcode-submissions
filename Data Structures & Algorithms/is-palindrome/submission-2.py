class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = []
        for char in s.lower():
            if char.isalnum() == False:
                continue
            s_list.append(char)
        for i in range(len(s_list) // 2):
            right = len(s_list) - i - 1
            if s_list[i] != s_list[right]:
                return False
        return True