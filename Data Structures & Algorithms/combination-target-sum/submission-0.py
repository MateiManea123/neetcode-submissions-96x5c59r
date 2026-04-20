class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(remain,index, path):
            if remain == 0:
                result.append(list(path))
                return 
            if remain < 0 or index == len(nums):
                return

            path.append(nums[index])
            backtrack(remain-nums[index],index,path)
            path.pop()

            backtrack(remain, index+1,path)
        
        backtrack(target,0,[])
        return result

            

