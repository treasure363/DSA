//Best Approach
class Solution{
    public int numIdenticalPairs(int[] nums){
        int ans = 0;
        //acc to constraints 1 <= nums[i] <= 100 so creating an array of different index whose values represent there total occurence
        int[] count = new int[101];
        for(int n: nums)//for each element in nums update the newly created array by 1[total occurence count]
            count[n]++;
        for(int n: count)//main logic
            ans += (n * (n - 1))/2;
        return ans;
    }
}

/*
    Brute Force
    int ans = 0;
    for(int i = 0; i < nums.length-1; i++) {
        for(int j = i+1; j < nums.length; j++) {
            if(nums[i] == nums[j])
                ans++;
        }
    }
    return ans;
*/

/*
    HashMap approach
    HashMap<Integer, Integer> hashMap = new HashMap<Integer, Integer>();
    int ans = 0;

    for (int num : nums) {
        if (hashMap.containsKey(num)) {
            hashMap.put(num, hashMap.get(num) + 1);
        } else {
            hashMap.put(num, 1);
        }
    }

    for(Integer key : hashMap.keySet()){
        if(hashMap.get(key) > 1){
            ans += hashMap.get(key) * (hashMap.get(key) - 1) / 2;
        }
    }
    return ans;
*/