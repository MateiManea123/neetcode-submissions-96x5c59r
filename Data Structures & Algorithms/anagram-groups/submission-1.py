class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashd = {}
        for string in strs:
            new_string = "".join(sorted(string))
            if new_string in hashd:
                hashd[new_string].append(string)
            else:
                hashd[new_string] = [string]

        return list(hashd.values())
        
        