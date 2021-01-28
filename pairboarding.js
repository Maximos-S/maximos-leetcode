const fib = (n, array) => {
    if (n <= 2) {
        return 1
    }
    let fibNum = fib(n-2, array) + fib(n-1, array)
    array.push(fibNum)
    return fibNum
}

const fibsSum = (n) => {
    fibNums = [1,1]
    fib(n, fibNums)
    let sum = 0;
    fibNums.forEach(num => {
        sum += num
    })
    return sum
}

console.log(fibsSum(4))