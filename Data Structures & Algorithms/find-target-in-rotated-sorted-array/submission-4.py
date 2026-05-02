class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_min(nums):
            l,r = 0, len(nums)-1
            minnum = nums[0]
            minpos = 0
            while l<=r:
                if nums[l] < nums[r]:
                    return (min(minnum,nums[l]),l)
                mid = (l+r)//2
                if nums[mid] < minnum:
                    minnum = nums[mid]
                    minpos = mid
                if nums[mid] >= nums[l]:
                    l = mid+1
                else:
                    r = mid-1
            return (minnum,minpos)
        def bsearch(nums,l,r):
            while l<=r:
                mid = (l+r)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1


        if nums[0] < nums[len(nums)-1]:
            return bsearch(nums,0,len(nums)-1)
        print(find_min(nums))
        (min_num,min_pos) = find_min(nums)

        if min_num == target:
            return min_pos
        
        if target > min_num and target < nums[0]:
            return bsearch(nums,min_pos,len(nums)-1)
        else:
            return bsearch(nums,0,min_pos)


                
            
            
            