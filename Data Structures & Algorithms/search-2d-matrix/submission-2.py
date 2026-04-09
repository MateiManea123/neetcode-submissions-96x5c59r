class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix)-1

        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        
        print(top,bot)

        if not top <= bot:
            return False

        l = 0
        r = len(matrix[0])-1

        while l<=r:
            mid2 = (l+r)//2

            if matrix[row][mid2] < target:
                l=mid2+1
            elif matrix[row][mid2] > target:
                r=mid2-1
            else:
                return True

        return False



