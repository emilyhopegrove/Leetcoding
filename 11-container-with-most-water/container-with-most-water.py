class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        # Calculate the initial max area based on the widest container possible
        max_water = (right - left) * min(height[left], height[right])
        
        #once the left and right pointers meet, stop the loop
        while left < right:
            #figure out the lengths and heights
            length = right - left
            current_height = min(height[left], height[right])
            area = length * current_height
            max_water = max(max_water, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water