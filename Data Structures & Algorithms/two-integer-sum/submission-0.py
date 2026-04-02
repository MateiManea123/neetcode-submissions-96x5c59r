class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for k,v in enumerate(nums):
            hm[v] = k

        for k,v in enumerate(nums):
            complement = target - nums[k]
            if complement in hm and hm[complement] != k:
                return [k, hm[complement]]