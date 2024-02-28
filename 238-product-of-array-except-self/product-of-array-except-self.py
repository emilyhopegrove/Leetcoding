class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Input: list of nums
        #output: list of nums 
        #approach: create two sub arrays, one for the left of the current index, and one for the right of the current index
        #each sub array should be the same length as the given nums array
        #traverse each sub array and store the product of each of the elements within
        #Multiply both sub arrays to produce the final product. This will effectively create a product that skips the current list


        #find the length of the given nums
        nums_length = len(nums)

        #create the left and right lists, and the results list and build them to be the same length as the given nums list
        left_list, right_list, result_list = [1] * nums_length, [1] * nums_length, [1] * nums_length 
        #Loop the left list and find its product
        for i in range(1, nums_length):
            #left list number is equal to the product of the character to the left of the current char in nums, times the character to the left of the current char in left list
            left_list[i] = nums[i - 1] * left_list[i - 1]


        #loop the right list and find its product
        for i in range(nums_length-2, -1, -1):
        #Multiply both by each other to find the final product
            right_list[i] = nums[i + 1] * right_list[i + 1]

        for i in range(nums_length):
            result_list[i] = left_list[i] * right_list[i]

        #return the product
        return result_list