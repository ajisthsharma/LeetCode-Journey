class Solution:
    def completePrime(self, num: int) -> bool:
        def is_prime(n):
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            
            i = 5
            
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6

            return True

        if num==2 or num==3 or num==5 or num==7:
            return True
        
        prefix = num
        while prefix > 0:
            if not is_prime(prefix):
                return False
            prefix //= 10
        
        divisor = 10
        while divisor <= num:
            suffix = num % divisor
            if not is_prime(suffix):
                return False
            divisor *= 10
        
        return True