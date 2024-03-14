class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #use a stack to manage the data, if the stack finishes by being empty that means we found a match for each char
        #map the closes to the opens
        #parse the string, check to see if each character is in the map
        #Remove from stack as you find pairs

        stack = []
        closeToOpen = {")":"(","]":"[","}":"{"}
        #Loop the string to parse out the characters
        #Loop the map to access each key
        for char in s:
            if char in closeToOpen:
                #if the stack is not empty, and the closing character in the map matches the last char in the stack
                if stack and stack[-1] == closeToOpen[char]:
                    #then remove it from the stack
                    stack.pop()
                else:
                    #otherwise if it doesn't match, that's a fast fail return false
                    return False
            else:
                #if we find an open parenthesis, then add it to the stack
                stack.append(char)
        #if the stack is empty, return true, otherwise it's false because there is an unmatched paren
        return not stack



