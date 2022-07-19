class Solution {
    public int[] createTargetArray(int[] nums, int[] index) {
        int[] out = new int[nums.length];
        for(int i=0; i<nums.length; ++i){
            //pulling/shifting the values from index[i]th position in the array out
            for(int j=nums.length-1; j>index[i]; --j)
                out[j] = out[j-1];
            out[index[i]] = nums[i];//adding nums[i] to the index[i]th position after creating the space for it
        }
        return out;
    }
}