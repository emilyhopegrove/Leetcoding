class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #Inputs; array of strings
        #output: Array of arrays with strings in them, each subset of arrays contains a group of anagram strings
        #Hash table - create an empty hash table to be used as a tracker
        #sort all of the given strings
        #store the sorted strings into tuples so that they can be used as keys in the hashtable
        #create the conditional block to check to see if the sorted string is in the hashtable
            #if it's not, add it as the key to the hashtable
            #if it is, append it as a string to the hashtable
        #return the hash table as a list

        #create a dict to be used for tracking the anagrams
        anagrams = {}
        #parse the strings
        for str in strs:
            #sort the string, store in tuple so that we can use the tuple as a key in the anagrams dict
            sorted_str = tuple(sorted(str))

            if sorted_str not in anagrams:
                #initialize a list of anagrams in the dictionary for a new anagram group 
                #that hasn't been encountered yet
                anagrams[sorted_str] = [str]
            else:
                #If the sorted string is in the anagrams dict, then append the str to the dict
                anagrams[sorted_str].append(str)

        #extract the values and return, disposing of the keys since they were used just for grouping purposes
        return list(anagrams.values())

