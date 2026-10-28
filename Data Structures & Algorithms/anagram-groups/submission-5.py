class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        search_dict = defaultdict(list)
        for _str in strs:
            count = [0] * 26
            for _char in _str:
                count[ord(_char) - ord("a")] += 1
            key = tuple(count)
            search_dict[key].append(_str)
        return list(search_dict.values())