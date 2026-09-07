class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = "+-/*"
        for item in tokens:
            if item not in operators:
                stack.append(int(item))
            else:
                match item:
                    case "+": 
                        stack.append(stack.pop() + stack.pop())
                    case "-": 
                        stack.append(-stack.pop() + stack.pop())
                    case "*": 
                        stack.append(stack.pop() * stack.pop())
                    case "/":
                        a, b = stack.pop(), stack.pop()
                        stack.append(int(float(b) / a))
        return stack[0]