class Solution:
    def maxArea(self, height: List[int]) -> int:

        left = 0

        right = len(height) - 1

        current_max = 0

        while left != right:

            #get lowest height of the two pointers
            if height[left] > height[right]:
                lowest_height = height[right]
                container = (right - left) * lowest_height
                right -= 1
            else:
                lowest_height = height[left]
                container = (right - left) * lowest_height
                left += 1

            if current_max < container:
                current_max = container

        return current_max
