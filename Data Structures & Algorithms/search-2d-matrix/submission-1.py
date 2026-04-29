class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            left = 0
            right = len(row) - 1
            print(row)
            if row[left] <= target <= row[right]:
                while True:
                    print("pair: ", left, right)
                    mid = (left + right) // 2
                    print("mid: ", mid)
                    if row[mid] == target:
                        return True
                    
                    if left > right:
                        return False
                    
                    if row[mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
        return False

        