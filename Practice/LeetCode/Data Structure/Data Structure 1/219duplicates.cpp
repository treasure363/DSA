class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        map<int, int> dup;
        for(int i=0; i<nums.size(); ++i)
            try
                dup.insert(pair<int, int>(nums[i], dup.get();
    }
};
/*
class Solution(object):

    def diff(self, arr, k):
        #print(arr)
        for i in range(len(arr)):
            for j in range(len(arr)):
                #print(i, j, abs(arr[i]-arr[j]), k)
                if abs(arr[i]-arr[j])<=k and i!=j:
                    return True
        return False
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dup = {}
        for i in range(len(nums)):
            try:
                dup[nums[i]].append(i)
            except:
                dup[nums[i]] = [i]
        for i in dup.keys():
            if len(dup[i])>1:
                if(self.diff(dup[i], k)):
                    return True
        return False
*/