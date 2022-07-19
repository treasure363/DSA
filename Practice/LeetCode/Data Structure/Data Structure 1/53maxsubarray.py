class Solution(object):
    def sumSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = -2147483648
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum = curr_sum + nums[i]
            if (sum < curr_sum):
                sum = curr_sum
    
            if curr_sum < 0:
                curr_sum = 0  
        return sum

p = Solution()
arr = [5,4,-1,7,8]
print(p.sumSubArray(arr))        