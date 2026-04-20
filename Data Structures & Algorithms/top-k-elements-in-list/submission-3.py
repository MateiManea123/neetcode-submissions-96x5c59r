class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]

        hm = {}
        res = []
        for num in nums:
            hm[num] = 1+ hm.get(num,0)

        for i,n in enumerate(hm):
            freq[hm[n]].append(n)
        
        freq = freq[::-1]
        for li in freq:
            if li != []:
                for elem in li:
                    res.append(elem)
                    k-=1
                    if k==0:
                        return res
        
        return []
                