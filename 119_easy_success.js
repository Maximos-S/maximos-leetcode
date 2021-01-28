//try to get the space down, overwrite the line before and use a while loop
var getRow = function (rowIndex) {
    let arr = []
    arr[0] = [1]
    if (rowIndex === 0) return arr
    arr[1] = [1, 1]
    if (rowIndex === 1) return arr[1]
    for (let i = 2; i <= rowIndex; i++) {
        arr[i] = []
        arr[i][0] = 1
        for (let j = 1; j < arr[i - 1].length; j++) {

            arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]
        }
        arr[i].push(1)
    }
    return arr[rowIndex]
};