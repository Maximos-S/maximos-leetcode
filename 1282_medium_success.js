class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        for idx in range(len(groupSizes)):
            try:
                groups[groupSizes[idx]].append(idx)
            except:
                groups[groupSizes[idx]] = [idx]
                
        resList = []
        
        for value in groups:
            numberGroups = len(groups[value]) // value
            
            for group in range(numberGroups):
                resList.append(groups[value][0:value])
                groups[value] = groups[value][value:]
        return resList
        