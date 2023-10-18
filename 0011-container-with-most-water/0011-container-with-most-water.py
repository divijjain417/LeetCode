class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_index = 0
        right_index = len(height) - 1
        maxArea = -1
        currArea = 0
        while (left_index < right_index):
            currArea = min(height[left_index], height[right_index])*(right_index - left_index)
            maxArea = max(maxArea,currArea)
            if (height[left_index] <= height[right_index]):
                left_index += 1
            elif (height[left_index] > height[right_index]):
                right_index -= 1
        return maxArea



        