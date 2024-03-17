class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #keep track of the current sequence of parentheses being built
        stack = []
        #provide a bucket for the results
        results = []

        def parensTracker(openers, closers):
            # Base case: same number of closers as openers, which also must equal n
            if openers == closers == n:
                #take all the string elements in the stack list and concatenates them into a single string. Use "".join(...) method
                results.append("".join(stack))
                #capture the current valid parentheses string from the stack and stores it in the results list
                return
            
            # Add in openers, so long as there are less openers than n
            if openers < n:
                stack.append("(")
                parensTracker(openers + 1, closers)
                stack.pop()

            # Add in closers, so long as there are less closers than openers
            if closers < openers:
                stack.append(")")
                parensTracker(openers, closers + 1)
                stack.pop()

        # Start the tracker
        parensTracker(0, 0)

        return results



        


        