class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hs = defaultdict(list)
        for string in strs:
            hs[''.join(sorted(string))].append(string)
        return list(hs.values())
        

