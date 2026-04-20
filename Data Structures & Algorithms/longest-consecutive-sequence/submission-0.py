class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)

        maxi = 0
        for num in numset:
            if num-1 not in numset:
                length = 0
                while (num+length) in numset:
                    length+=1
                maxi = max(maxi, length)
        return maxi

