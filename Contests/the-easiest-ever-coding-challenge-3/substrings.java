import java.io.*;
import java.util.*;

class GFG { // Drivers Code Start
    public static void main(String[] args) throws IOException{
        BufferedReader read = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());

        while(t-- > 0) {
            String S = read.readLine().trim();
            Solution ob = new Solution();
            int ans = ob.countSubstring(S);
            System.out.println(ans);
        }
    }
} // Drivers Code End

//User function Template for Java
class Solution { 
    int countSubstring(String S) { 
        // code here
        int len = S.length();
        int[][] arr = new int[len][len];
        for (int[] row : arr)
        Arrays.fill(row, 0);
        // for (int[] row : arr)
        //     System.out.println(Arrays.toString(row) + "\n");
        int l, r;
        for(int i = 0; i < len; ++i) {
            arr[i][i] = 1;
            if (Character.isUpperCase(S.charAt(i))) {
                l = 65;
                r = 90;
            }
            else {
                l = 97;
                r = 122;
            }
            for(int j = i + 1; j < len; ++j) {
                // if(arr[i][j - 1] == 0)
                //     continue;
                if(S.charAt(j) >= l && S.charAt(j) <= r)
                    arr[i][j] = arr[i][j - 1] + 1;
                else
                    arr[i][j] = arr[i][j - 1] - 1;
            }
        }
        //count zero
        int count = 0;
        for(int i = 0; i < len; ++i)
            for(int j = i + 1; j < len; ++j) 
                if(arr[i][j] == 0) count ++;
        // for (int[] row : arr)
        //     System.out.println(Arrays.toString(row));
        // System.out.println("Count = " + count);
        
        return count;
    }
} 
