class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicti = dict()
        ans = list()
        for num in nums:
            if num in dicti:
                dicti[num] +=1
            else:
                dicti[num] = 1

        sorted_dict = dict(reversed(sorted(dicti.items(), key=lambda item: item[1])))
        j=0
        for i in sorted_dict:
            if j<k:
                ans.append(i)
                j+=1

        return ans
            


        
        