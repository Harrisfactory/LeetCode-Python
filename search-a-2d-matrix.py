class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        nums = []

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                nums.append(matrix[i][j])

        left = 0

        right = len(nums) - 1

        while left <= right:

            middle = (left + right) // 2

            if nums[middle] == target:
                return True
            elif nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1

        return False

    #brute force
