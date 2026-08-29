class Solution:
    def maxArea(self, heights: List[int]) -> int:
        candidate = 0
        start = 0
        end = len(heights)-1
        while start != end:
            area = (end-start) * min(heights[end],heights[start])
            if area > candidate:
                candidate = area
            if heights[start] > heights[end]:
                end -= 1
            else:
                start += 1
        return candidate