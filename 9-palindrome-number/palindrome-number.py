class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        #convert to a string
        #reverse it
        #convert back to integer
        #Check if reversed integer and original integer match
        #if not return false
        #otherwise return true
        #fast fail if lengths don't match
        string_x = str(x)
        reversed_num = string_x[::-1]

        if len(reversed_num) != len(string_x):
            return false
        
        elif string_x == reversed_num:
            return True
        
        return False

