var generate = function (numRows) {
    let arr = []
    if(numRows === 0) return arr
    arr[0] = [1]
    if(numRows === 1) return arr
    arr[1] = [1, 1]
    for (let i = 2; i < numRows; i++) {
        arr[i] = []
        arr[i][0] = 1
        for (let j = 1; j < arr[i - 1].length; j++) {

            arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]
        }
        arr[i].push(1)
    }
    return arr
};
console.log(generate(5))