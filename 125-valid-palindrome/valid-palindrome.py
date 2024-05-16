class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #Clean up
        s = ''.join(char.lower() for char in s if char.isalnum())
        #set up the 2 pointers
        l = 0
        r = len(s) - 1

        #check to see if l = r, if so incriment left by 1 and decrement r by 1. otherwise return false
        #keep going until l and r meet. if all are equal, return true        
        while l < r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        return True
