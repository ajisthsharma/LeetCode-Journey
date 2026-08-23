class Solution {
public:
    vector<int> getSumAbsoluteDifferences(vector<int>& nums) {
        vector<int> res;
        int prefixSum = 0;
        int suffixSum = 0;

        for (int num : nums) {
            suffixSum += num;
        }

        for (int i = 0; i < nums.size(); i++) {
            int leftSum = nums[i] * i - prefixSum;
            int rightSum = suffixSum - nums[i] * (nums.size() - i);
            int totalSum = leftSum + rightSum;

            res.push_back(totalSum);

            prefixSum += nums[i];
            suffixSum -= nums[i];
        }

        return res;        
    }
};