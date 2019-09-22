class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        uniqNum = nums[0]
        
        for i in range(1, len(nums)):
            uniqNum ^= nums[i]
        
        return uniqNum
        