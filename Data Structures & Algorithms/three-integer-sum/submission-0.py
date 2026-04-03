class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        sol = []
        l,r = 0,  len(nums)-1

        for i in range(len(nums)):
            l,r=i+1,len(nums)-1
            while l<r:
                sum = nums[i] + nums[l] + nums[r]
                if sum < 0:
                    l+=1
                elif sum > 0:
                    r-=1
                else:
                    if not [nums[i], nums[l], nums[r]] in sol:
                        sol.append([nums[i], nums[l], nums[r]])
                    l+=1

        return sol