class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int s=0;
        int n=mat.size();
        for(int i=0;i<n;i++){
            s+=mat[i][i];
            s+=mat[i][n-1-i];
        }
        if(n%2!=0)
        {
            s-=mat[n/2][n/2];
        }
        return s;   
    }    
};