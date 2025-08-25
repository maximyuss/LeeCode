// https://leetcode.com/problems/diagonal-traverse/
class Solution {
    public int[] findDiagonalOrder(int[][] mat) {
        if (mat.length == 0 || mat[0].length == 0)
            return new int[0];
        
        int m = mat.length, n = mat[0].length;
        int row = 0, col = 0;
        int[] res = new int[m * n];
        boolean up = true;

        for (int i = 0; i < m * n; i++) {
            res[i] = mat[row][col];

            if (up) {
                if (col == n - 1) {
                    row++;
                    up = false;
                } else if (row == 0) {
                    col++;
                    up = false;
                } else {
                    row--;
                    col++;
                }
            } 
            else {
                if (row == m - 1) {
                    col++;
                    up = true;
                } else if (col == 0) {
                    row++;
                    up = true;
                } else {
                    row++;
                    col--;
                }
            }
        }
        return res;
    }
}
