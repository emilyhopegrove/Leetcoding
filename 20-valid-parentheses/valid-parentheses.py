class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #regex?
        #broootforce
        #If else - loop and match
        #loop through the string, so if the char matches "(" or ")" or "[" or "]" or "{" or "}"
        #then hold the char in a container and check to see if its pair is in another container
        #could house the incorrect pairs and see if there's a match then return false
        #if yes then return true. otherwise false
        #Fast fail, could loop the string and if the first char is not an opener, return false

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



