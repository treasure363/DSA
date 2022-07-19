class Solution {
    public int maxSubArray(int[] nums) {
        int sum = Integer.MIN_VALUE, curr_sum=0;
        for(int i=0; i<nums.length; ++i){
            curr_sum += nums[i];
            if(curr_sum>sum)
                sum=curr_sum;
            if(curr_sum<0)
                curr_sum=0;
        }
        return sum;
    }
}