class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        search_dict = {}
        for _str in strs:
            count = [0] * 26
            for _char in _str:
                count[ord(_char) - ord("a")] += 1
            key = tuple(count)
            if key in search_dict:
                search_dict[key].append(_str)
                continue
            search_dict[key] = [_str]
        return list(search_dict.values())