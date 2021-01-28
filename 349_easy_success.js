var intersection = function(nums1, nums2, resArr = []) {
    if(!nums1.length) {
        return resArr
    }
    if (!nums2.length) {
        return resArr
    }
    
    target = nums1.shift()
    let newArr2 = []
    let intersect
    let value
    
    nums2.forEach((num, idx) => {
        if (target === num) {
            intersect = true
            value = num
        } else {
            newArr2.push(num)
        }
    })
    if (intersect) {
        resArr.push(value)
    }
    return intersection(nums1, newArr2, resArr)
};