class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ""
        carry = 0


        #Revere the strings
        a = a[::-1]
        b = b[::-1]

        #loop through every character in both strings, convert the character into a digit
        for i in range(max(len(a), len(b))):
            #convert the character into the appropriate integer so long as it's within the range, otherwise default to 0
            digitA = int(a[i]) if i < len(a) else 0
            digitB = int(b[i]) if i < len(b) else 0
            #sum up the digits, add in the carry
            total = digitA + digitB + carry
            #recreate the characters but modulus by 2 because binary is base 2
            character = str(total % 2)
            #add the character to the resul bucket
            result = character + result
            #update the carry integer, divide total by 2 
            carry = total // 2
        #take care of edge cases. If carry is not 0, add a 1 to the result
        if carry:
            result = "1" + result
        return result
        