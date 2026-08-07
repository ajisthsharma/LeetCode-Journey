class Solution {
public:
    int minAddToMakeValid(string s) {
        int left = 0, right = 0;
        
        for (auto ch : s){
            if (ch == '(')
                left += 1;

            else if (ch == ')'){
                if (left > 0)
                    left -= 1;

                else
                    right += 1;
            }
        }
        
        return left + right;
    }
};