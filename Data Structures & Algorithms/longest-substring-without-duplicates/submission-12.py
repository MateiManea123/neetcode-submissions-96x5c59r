class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myset = set()
        l = 0
        r = 0
        if s:
            maxlen = 1
        else:
            return 0
        while r<len(s):
            while s[r] in myset:
                myset.remove(s[l])
                l+=1
            myset.add(s[r])
            print(myset)
            maxlen = max(maxlen,len(myset))
            r+=1

        return maxlen

        