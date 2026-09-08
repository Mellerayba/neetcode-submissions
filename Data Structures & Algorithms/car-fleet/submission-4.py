class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        array = []
        stack = []
        for i in range(len(speed)):
            array.append((position[i],speed[i]))
        array = sorted(array,reverse=True)
        for car in array:
            time = (target - car[0]) / car[1]
            if stack:
                if time>stack[-1]:
                    stack.append(time)
            else:
                stack.append(time)
        return len(stack)
        