class Solution {
    public List<Integer> luckyNumbers (int[][] matrix) {
        List<Integer> out=new ArrayList<Integer>();
        int r=matrix.length, c=matrix[0].length, min_r, max_c, col=0;
        for(int i=0; i<r; ++i)
        {
            min_r = 1000000;//storing minimum element of the current row
            max_c = -1;//storing maximum element of the column where the minimum element is present
            col = 0;//storing the column number of the minimum element of the current row
            for(int j=0; j<c; ++j)
                if(matrix[i][j]<min_r){
                    min_r=matrix[i][j];
                    col = j;
                }
            for(int j=0; j<r; ++j)
                if(matrix[j][col]>max_c)    
                    max_c=matrix[j][col];
            
            if(min_r==max_c)
                out.add(matrix[i][col]);
        }
        return out;
    }
}