class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        count_letters = {}

        for char_s, char_t in zip(s, t):
            #get the letters from s, if the letter isn't there, default its value to 0. otherwise, add 1 to its count. Then, get the letters from t, if the letter isn't there, default its value to 0. otherwise, subtract 1 from its count. If we 0 out then we have an anagram, otherwise it's not an anagram
            count_letters[char_s] = count_letters.get(char_s, 0) + 1
            count_letters[char_t] = count_letters.get(char_t, 0) - 1

        for count in count_letters.values():
            if count != 0:
                return False

        return True

        
