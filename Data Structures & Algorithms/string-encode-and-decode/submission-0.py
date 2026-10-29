class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for _str in strs:
            result += str(len(_str)) + "#"
            for _char in _str:
                result += _char
        
        print(result)
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            index = int(s.find("#", i))
            str_len = int(s[i:index])
            _str = s[index + 1:index + str_len + 1]
            result.append(_str)
            i = index + str_len + 1
        return result
