class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        #Create a results list, ensure it is the same length as the given temperatures list, 
            #and prepopulate it with 0s, handling for the end of the array and when there is no larger temp to the right
        #Create a stack memory bucket where pairs of info will be stored

        #For loop through the given array of temperatures, and enumerate to extract the each temp being looped over, and it's corresponding index location
            #while the handy dandy memory bucket stack is NOT EMPTY (meaning there's something in there!) 
            #and the current temperature that is being looped over is greater than the temp that is at the top of the stack
            #then get rid of that top item in the stack! pop it off - goodbye! adios! au revoir! 
                #Store the temp and index inside nifty variables usign tuple unpacking
            #Get the difference between the current index and the stackInd, and ppdate the results list @ the stackInd index with that difference. 
                #This is the number of days until the weather gets warmer 
            #put the current t(emp) and i(ndex) pair onto the end of the memory stack. 

        # in the results container, record the current temperature and its index to track future warmer days.
             #add the current day's temperature and its index to a stack because we have not yet found a 
             #future temperature that's warmer. The stack keeps track of all such temperatures,
              #in the order they were encountered. This ensures that whenever we do find a warmer temperature
              #on a subsequent day, we can easily update the correct positions in the result list 
              #with the number of days waited.

# The solution uses a stack to keep track of temperatures that haven't yet found a warmer future temperature. It iterates through the list of daily temperatures, and for each day's temperature:

# It looks at the stack of previously logged temperatures that are waiting for a warmer day. If the current temperature is warmer than the temperature at the top of the stack, it pops temperatures from the stack, calculates how many days were waited until this warmer day, and records this in the result list.

# It then adds the current day's temperature and its index to the stack because we need to start tracking how many days will pass until a warmer temperature is found for this day.

# It continues this process for all temperatures in the list.

# The result list is filled with the number of days that must be waited for a warmer temperature for each day. If no warmer temperature is found, the default value remains 0.

# The stack is used to efficiently find the next warmer temperature without the need to revisit temperatures that have already found a warmer day.

     # Initialize the result list with zeros for each day
        res = [0] * len(temperatures)
        # Stack to keep track of temperatures and their indices
        stack = []  # Each element is a pair: [temperature, index]

        # Iterate over the list of temperatures with their indices
        for i, t in enumerate(temperatures):
            # While there's a temperature on the stack and the current temperature is higher
            while stack and t > stack[-1][0]:
                # Pop the top temperature from the stack and get its index
                stackTemp, stackInd = stack.pop()
                # Calculate the number of days waited and update the result list
                res[stackInd] = i - stackInd
            # Add the current temperature and its index to the stack
            stack.append([t, i])
        # Return the result list with the days to wait for a warmer temperature
        return res

