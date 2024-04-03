class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])
            #if middle is greater than right, move left to right of the middle
            if nums[m] >= nums[l]:
                l = m + 1
            #otherwise move right to left of the middle
            else:
                r = m - 1
        return res