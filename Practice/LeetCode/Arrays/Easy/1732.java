class Solution {
    public int largestAltitude(int[] gain) {
        int[] out = new int[gain.length+1];
        for(int i=0; i<gain.length; ++i)
            out[i+1]=gain[i]+out[i];
        int max=out[0];
        for(int i=0; i<gain.length+1; ++i)
            if(out[i]>max)  max = out[i];
        return max;
    }
}