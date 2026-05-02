class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1
        minmid = nums[0]
        while l<=r:

            if nums[l] < nums[r]:
                return min(minmid,nums[l])
            mid =(l+r)//2
            print("mid:",mid)
            print("l:",l)
            print("r:",r)
            
            minmid = min(minmid,nums[mid])
            if nums[mid]>=nums[l]:
                l = mid+1
            elif nums[mid]<nums[r]:
                r = mid-1

        return minmid
            