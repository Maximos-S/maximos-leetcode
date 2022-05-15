# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n, previousState=False, index=0):
        """
        :type n: int
        :rtype: int
        """
        resultFound = False
        midPoint = n // 2
        smallest = 0
        largest = n
        version = isBadVersion(n)
        nextVersion = isBadVersion(n - 1)
        if version and not nextVersion:
            print("hits here")
            return n
        if n > 3:
            while not resultFound and midPoint > 0:
                version = isBadVersion(midPoint)
                nextVersion = isBadVersion(midPoint - 1)
                print(midPoint)
                if version and not nextVersion:
                    resultFound = True
                elif version:
                    previousLargest = midPoint
                    midPoint = midPoint - ((midPoint - smallest) / 2)
                    largest = previousLargest
                else:
                    prevSmallest = midPoint
                    midPoint = midPoint + ((largest - midPoint) / 2)
                    smallest = prevSmallest
        else:
            for i in range(1, n + 1):
                version = isBadVersion(i)
                nextVersion = isBadVersion(i - 1)
                if version and not nextVersion:
                    return i
        if midPoint == 0:
            return 1
        return int(midPoint)


#         if n == 1:
#             return index + 1
#         midPoint = midPoint // 2
#         badVersion = isBadVersion(midPoint)
#         if previousState != badVersion:
#             if not badVersion and isBadVersion(midPoint + 1):
#                 return index + 1

#         if badVersion:
#             return self.firstBadVersion(midPoint, badVersion, index)
#         else:
#             return self.firstBadVersion(n[midPoint:], badVersion, index + midPoint)
