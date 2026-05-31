class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        while l<= r:
            mid = (l+r)//2
            # print(mid)
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                i,j = 0, len(matrix[mid])-1
                while i<= j:
                    m = (i+j)//2
                    if target == matrix[mid][m]:
                        return True
                    elif target > matrix[mid][m]:
                        i = m +1
                    else:
                        j = m-1
                return False
            elif target > matrix[mid][-1]:
                l = mid + 1
            else:
                r = mid-1
        
        return False