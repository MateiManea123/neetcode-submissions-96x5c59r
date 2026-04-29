class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_entries = set()
        l = r= 0
        maxlen = 0
        while r < len(s):
            while s[r] in curr_entries:
                curr_entries.remove(s[l])
                l+=1
            curr_entries.add(s[r])
            r+=1
            maxlen = max(maxlen,r-l)
        return maxlen
             
        