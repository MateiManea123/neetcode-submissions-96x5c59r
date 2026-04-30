class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def backtrack(total,i,path):
            if total == target:
                result.append(path.copy())
                return
            if total > target or i == len(candidates):
                return

            path.append(candidates[i])
            backtrack(total+candidates[i],i+1,path)

            path.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            backtrack(total,i+1,path)

        backtrack(0,0,[])
        return result

            
            

