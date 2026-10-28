class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        search_dict = defaultdict(list)
        for _str in strs:
            key = ''.join(sorted(_str))
            search_dict[key].append(_str)
        return list(search_dict.values())