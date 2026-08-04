# Last updated: 04/08/2026 11:37:00
class Solution(object):
    def carFleet(self, target, position, speed):

        pairs = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)

        stack = []

        for p, s in pairs:
            time = (target - p) / s

            if stack and time <= stack[-1]:
                continue

            stack.append(time)

        return len(stack)