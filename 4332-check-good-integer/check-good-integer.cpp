class Solution {
public:
    bool checkGoodInteger(int n) {
        int digit_sum=0,square_sum=0;

        while (n>0){
            int digit=n%10;
            digit_sum+=digit;
            square_sum+=digit*digit;
            n/=10;
        }

        return (square_sum-digit_sum)>=50;
    }
};