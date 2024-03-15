class MinStack(object):

    def __init__(self):
        #keep track of all the things
        self.stack = []
        #just keep track of the smallest things
        self.minStack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        #take the input value and append to the stack
        self.stack.append(val)
        #decide what is the smallest value then append to the min stack. 
        #Set val to the smaller of the new value or the smallest value currently in the stack. If the stack is empty, just keep val as it is.
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        #Just return the last thing that was put on top of the main stack
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        #since the minstack will now have the smallest thing on the top, just return that value 
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()