class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            x *= -1
            negative = True
        new_num = 0
        while x >= 10:
            new_num *= 10
            new_num += x % 10
            x = x//10
        new_num *= 10
        new_num += x
        if negative:
            new_num *= -1
        if -2**31 <= new_num and new_num <= 2**31:
            return new_num
        else:
            return 0
