class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        search_dict = defaultdict(list)
        for _str in strs:
            count = [0] * 26
            for _char in _str:
                count[ord(_char) - 97] += 1
            search_dict[tuple(count)].append(_str)
        return list(search_dict.values())