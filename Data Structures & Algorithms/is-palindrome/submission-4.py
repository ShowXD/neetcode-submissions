class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_list = []
        for char in s.lower():
            if char.isalnum() == False:
                continue
            s_list.append(char)
        for index, char in enumerate(s_list):
            if index == len(s_list) / 2:
                return True
            left = index
            right = len(s_list) - index - 1
            if s_list[left] != s_list[right]:
                return False
        return True