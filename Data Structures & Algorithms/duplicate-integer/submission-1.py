class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hs = set(nums)
        print(hs)
        if len(hs) != len(nums):
            return True
        return False

