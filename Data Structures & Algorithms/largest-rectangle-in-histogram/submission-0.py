class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        currentMax = 0
        boundaries = []

        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                index,height = stack.pop()
                currentMax = max(currentMax,(i-index)*height)
                start = index
            stack.append((start,heights[i]))
        while stack:
            index,height = stack.pop()
            area = height * (len(heights)-index)
            currentMax = max(currentMax,area)
        return currentMax


