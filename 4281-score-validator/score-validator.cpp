class Solution {
public:
    vector<int> scoreValidator(vector<string>& events) {
        int score=0,count=0;

        for (auto ch: events){
            if (ch=="W")
                count+=1;

            else if (ch=="WD" or ch=="NB")
                score+=1;

            else
                score+=stoi(ch);

            if (count==10) break;
        }

        return {score,count};
    }
};