class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = {}
        for i in nums:
            if i not in visited:
                visited[i] = 1
            else:
                del visited[i]

        for i in visited:
            return i
# dumb way to do it:
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         sortedNums = self.mergeSort(nums)
#         print(sortedNums)
#         i = 0
#         for j in range(len(nums)):
#             if i >= len(nums) - 1:
#                 return sortedNums[len(nums)-1]
#             print(sortedNums[i])
#             print(sortedNums[i+1])
#             if sortedNums[i] != sortedNums[i+1]:
#                 return sortedNums[i]
#             i += 2

#     def mergeSort(self, nums):
#         if len(nums) <= 1:
#             return nums
#         mid = math.floor(len(nums)/2)

#         leftSorted = self.mergeSort(nums[0:mid])
#         rightSorted = self.mergeSort(nums[mid:])

#         return self.merge(leftSorted, rightSorted)

#     def merge(self, leftList, rightList):
#         newList = []
#         while len(leftList) and len(rightList):
#             if leftList[0] <= rightList[0]:
#                 newList.append(leftList.pop(0))
#             else:
#                 newList.append(rightList.pop(0))
#         if len(leftList):
#             newList += leftList
#         if len(rightList):
#             newList += rightList
#         return newList
