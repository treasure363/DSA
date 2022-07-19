class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            try:
                d[nums[i]].append(i)
            except:
                d[nums[i]] = [i]
        ans = []
        for i in d.keys():
            rem = target - i
            try:
                if(i!=rem):
                    ans = [d[i][0],d[rem][0]]
                    break
                elif(len(d[i])!=1):
                    ans = [d[i][0],d[rem][1]]
                    break
            except:
                pass
        return ans

p=Solution()
arr = [-1,-2,-3,-4,-5]
print(p.twoSum(arr, -8))