def isHappy(n):
        digits = []
        
        while n >= 10:
            digits.append(n % 10)
            n //= 10
        digits.append(n)
        
        sum = 0
        
        for digit in digits:
            sum += digit**2
        if sum == 1:
            return True
        else:
            try:
                return isHappy(sum)
            except:
                return False




print(isHappy(19))