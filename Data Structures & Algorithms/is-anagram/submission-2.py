class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqs = {}
        freqt = {}

        for string in s:
            freqs[string] = 1 + freqs.get(string,0)
        
        for string in t:
            freqt[string] = 1 + freqt.get(string,0)

        if freqs != freqt:
            return False
        return True
        