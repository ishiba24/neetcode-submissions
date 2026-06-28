class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p,s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:
            speed = ((target - p) / s)
            if stack and stack[-1] >= speed:
                continue
            stack.append(speed)
        return len(stack)