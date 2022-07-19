class Solution {
    public int[][] flipAndInvertImage(int[][] image) {
        int n = image.length;
        int[][] out = new int[n][n];
        for(int i=0; i<n; ++i)
            for(int j=n-1; j>=0; --j)
                out[i][n-j-1]= (image[i][j]==1)?0:1;
        return out;
    }
}