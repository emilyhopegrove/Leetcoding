class Solution(object):
    def carFleet(self, target, position, speed):
        """
        The function calculates the number of car fleets that will arrive at the target.
        A car fleet is formed when a faster car catches up to a slower one before or at the target, 
        and they proceed together at the slower car's speed.

        :param target: The target distance from the start.
        :param position: A list of starting positions of the cars.
        :param speed: A list of speeds of the cars.
        :return: The total number of car fleets that will reach the target.
        """
        # Pair each car's position with its speed and sort them in reverse order based on their position.
        # This way, cars closer to the target are considered first.
        positionSpeedPair = sorted(zip(position, speed), reverse=True)
        
        stack = []  # This stack will hold the times at which each car (or fleet) reaches the target.
        
        # Iterate through each car, considering its position and speed.
        for p, s in positionSpeedPair:
            # Calculate the time it takes for the current car to reach the target.
            timeToReachTarget = (target - p) / float(s)
            
            # If the current car does not catch up to the car in front of it (or it's the first car),
            # it forms a new fleet. This is checked by comparing its time to the last item in the stack.
            # Only add this time to the stack if it's strictly greater than the last time in the stack,
            # indicating that it doesn't catch up to the car/fleet in front.
            if not stack or timeToReachTarget > stack[-1]:
                stack.append(timeToReachTarget)
                
        # The stack's length represents the number of separate times cars/fleets reach the target,
        # which is equivalent to the number of fleets.
        return len(stack)


