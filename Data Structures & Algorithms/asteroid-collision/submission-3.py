class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #if we've added an element and the next is opp sign, they will run into each other
        stack = []
        for ast in asteroids:
            while stack and ast < 0 and stack[-1] > 0:
                if abs(ast) > abs(stack[-1]):
                    stack.pop()
                elif abs(ast) < abs(stack[-1]):
                    ast = 0
                else:
                    ast = 0
                    stack.pop()
            if ast:
                stack.append(ast)
        return stack
        
                    