class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #Solution 1: Make it work
        #Keep track of the number of each letter in each string, 
        #then check to see if there is a match of dictionaries
        #Could use the fast fail approach to see if the lengths are the same - if not, return false right away
        
        #Fast fail: Return false if the lengths aren't the same
        # if len(s) != len(t):
        #     return False

        # s_char_tracker = {}
        # t_char_tracker = {}
        # #Build the s dict
        # for char in s:
        #     if char in s_char_tracker:
        #         s_char_tracker[char] += 1
        #     else:
        #         s_char_tracker[char] = 1
        # #Build the t dict
        # for char in t:
        #     if char in t_char_tracker:
        #         t_char_tracker[char] += 1
        #     else:
        #         t_char_tracker[char] = 1

        # return s_char_tracker == t_char_tracker

        #Solution 2: Make it better
        #Use a single dictionary after the fast fail establishes they are the same length

        char_count = {}

        #use the get method to count the number of times a character occurse
        #if the s char is in the dictionary add 1 to its count, otherwise default it to 0
        #if the t char is in the dictionary, subtract 1 from its count, otherwise default it to 0
        #This way, for every char in s string, if there's a corresponding char in t, it will 0 out
        #to produce an anagram
        if len(s) != len(t):
            return False
            
        for i in range(len(s)):
            char_count[s[i]] = char_count.get(s[i], 0) + 1
            char_count[t[i]] = char_count.get(t[i], 0) - 1
        
        #Extract the values from the char count dictionary. If the value is not 0, 
        #that indicates that there is an uneven number of letters in s or t so it's not an anagram

        for count in char_count.values():
            if count != 0:
                return False

        #OTHERWISE return true
        return True

