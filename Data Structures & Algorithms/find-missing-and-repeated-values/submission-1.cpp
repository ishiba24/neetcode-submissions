class Solution {
public:
    vector<int> findMissingAndRepeatedValues(vector<vector<int>>& grid) {
        unordered_map<int, int> freqMap;
        vector<int> ans;
        for (int r = 0; r < grid.size(); r ++){
            for (int c = 0; c < grid[r].size(); c ++){
                freqMap[grid[r][c]]++;
            }
        }
        for (auto&p: freqMap){
            int num = p.first;
            int count = p.second;
            if (count == 2){
                ans.push_back(p.first);
            }
        }
        int n = grid.size();
        for (int num = 1; num <= n*n; num++){
            if (freqMap.find(num) == freqMap.end()){
                ans.push_back(num);
                break;
            }
        }
        return ans;
    }
};