class Solution {
    public int[] sumZero(int n) {
        int[] out = new int[n];
        for(int i=0; i<n-1; i+=2){
            out[i] = i+1;
            out[i+1] = -i-1;
        }
        return out;
    }
}