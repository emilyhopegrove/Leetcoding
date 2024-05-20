class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Mapping of closing brackets to corresponding opening brackets
        bracket_map = {"]": "[", "}": "{", ")": "("}
        open_brackets = bracket_map.values()
        bracket_tracker = []
        
        # Iterate through each character in the string
        for char in s:
            if char in open_brackets:
                # If it's an open bracket, push it onto the stack
                bracket_tracker.append(char)
            elif char in bracket_map:
                # If it's a closing bracket, check for a matching open bracket
                if bracket_tracker and bracket_tracker[-1] == bracket_map[char]:
                    bracket_tracker.pop()
                else:
                    return False
        
        # Check if the stack is empty (all brackets matched correctly)
        return len(bracket_tracker) == 0
        
        
        
        
#Time and space complexity are both O(n) 
    #We are iterating through the string only once, where n is the length of the string. For each character, we are performing a constant amount of work (either pushing onto the stack or popping from it). Hence, the time complexity is O(n). In the worst-case scenario, all characters in the string are opening brackets, and we push all of them onto the stack. Hence, the space complexity is O(n), where n is the length of the string.


