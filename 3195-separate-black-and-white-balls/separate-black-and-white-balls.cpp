class Solution {
public:
    long long minimumSteps(string s) {
        long long swap=0;
        int black=0;

        for (auto ball : s){
            if (ball=='0')
                swap+= (long long) black;
            else
                black+=1;
        }

        return swap;
    }
};