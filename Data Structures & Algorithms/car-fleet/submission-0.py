class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        time_stack = []
        for pos, spd in cars:
            car_time = (target - pos) / spd
            if not time_stack or time_stack[-1] < car_time:
                time_stack.append(car_time)
            
        return len(time_stack)
