class Solution {
public:
    int smallestNumber(int n, int t) {
        int prod=1;
        
        for( int i=n; i<=100; i++){
            int temp=i;
            while (temp>0){
                prod*=temp%10;
                temp/=10;
            }
            if (prod%t==0)
                return i;
            
            prod=1;
        }
        return n;
    }
};