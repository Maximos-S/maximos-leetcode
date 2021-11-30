
def increasingTriplet(nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        smallNum = None
        secondNum = None
        for i in range(len(nums)):
            num = nums[i]
            if num < smallNum or smallNum == None:
                smallNum = num
            elif num < secondNum and num > smallNum or (secondNum == None and num > smallNum):
                secondNum = num
            elif secondNum < num and secondNum != None and secondNum != num:
                return True

        return False

