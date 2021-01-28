var divide = function (dividend, divisor) {
    let counter = 0;
    let dividendNegative = false;
    let divisorNegative = false;
    if(dividend < 0) {
        dividendNegative = true;
        dividend = -dividend
    }
    if(divisor < 0) {
        divisorNegative = true;
        divisor = -divisor
    }
    
    // if (divisor > dividend) return 0;
    if (divisor > 0) {
        while (dividend >= divisor) {
            counter++
            dividend -= divisor;
        }
        // divideRecur(dividend, divisor, counter)
    }

    if(dividendNegative) {
        counter = -counter
    }
    if(divisorNegative) {
        counter = -counter
    }
    if (counter >= 2147483648) counter--
    if (counter <= -2147483648) counter++
    return counter;
};

// function divideRecur(dividend, divisor, counter=0) {
    
// }


console.log(divide(5000,6000))