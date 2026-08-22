class Solution {
public:
    bool checkDivisibility(int n) {
        int temp=n;
        int summ=0;
        int prod=1;

        while (temp>0){
            int digit=temp%10;
            summ+=digit;
            prod*=digit;
            temp/=10;
        }

        return n%(summ+prod)==0;
    }
};