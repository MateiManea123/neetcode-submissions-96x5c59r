class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums = {}
        prefix_sums[0] = 1
        curr_sum = 0
        res = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            target = curr_sum - k
            if prefix_sums.get(target)!=None:
                res += prefix_sums[target]
            prefix_sums[curr_sum] = prefix_sums.get(curr_sum,0) + 1

        return res
