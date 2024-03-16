class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        #inputs: strings
        #outputs: a single integer
        #It's easy enough to handle for normal tokens that are just the numbers, intify and append to the results
        #for each of the operands, pop 2 nums off then run through how to append them. add and multiply are similar
        #subtraction and division are trickier - figure out division to handle for the special case where it always truncates towards 0

        # Stack to store numbers
        stack = []
        #parse the tokens
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                #name the numbers in order. Since in a stack we look at them from top to bottom, the top number we name first will be the second number
                num2 = stack.pop()  # Pop the second operand
                num1 = stack.pop()  # Pop the first operand
                
                if token == "+":
                    stack.append(num1 + num2)
                elif token == "-":
                    stack.append(num1 - num2)
                elif token == "*":
                    stack.append(num1 * num2)
                elif token == "/":
                    # Perform division and ensure truncation towards zero.
                    result = abs(num1) // abs(num2)
                    # Adjust the sign of the result only if the original operands had different signs.
                    result = result if (num1 > 0) == (num2 > 0) else -result
                    stack.append(result)
        
        return stack[0]  
