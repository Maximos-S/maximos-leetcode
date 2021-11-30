class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        squaredNums = [num * num for num in nums]

        sortedNums = self.mergeSort(squaredNums)

        return sortedNums

    def mergeSort(self, nums):

        if len(nums) == 1:
            return nums

        midPoint = len(nums) // 2

        leftArr = nums[:midPoint]
        rightArr = nums[midPoint:]

        sortedLeft = self.mergeSort(leftArr)
        sortedRight = self.mergeSort(rightArr)

        return merge(sortedLeft, sortedRight)

    def merge(self, arr1, arr2):
        resArr = []

        while len(arr1) and len(arr2):
            if arr1[0] > arr2[0]:
                resArr.append(arr1.pop(0))
            else:
                resArr.append(arr2.pop(0))

        if len(arr1):
            resArr = resArr + arr1
        else:
            resArr = resArr + arr2
        return resArr
