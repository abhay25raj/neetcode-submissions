typedef vector<int> vi;
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int n = nums.size();
        int l = n/2;
        unordered_map<int,int>f;
        for(auto v:nums)
        f[v]++;
        // int c  = 0;
        for(auto x:f)
        {
            if(x.second>l)
            return x.first;
        }
        return 0;
    }
};