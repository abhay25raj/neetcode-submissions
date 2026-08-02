class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int x = arr.size();
        for(int i=0;i<x-1;i++)
        {
            int n = -1;
            for(int j=i+1;j<x;j++)
            {
               n = max(n,arr[j]);
            }
            arr[i] = n;
        }
        arr[x-1] = -1;
        return arr;  
    }
};