class Solution:
    def __init__(self):
        self.pairs = {"{": "}", "[": "]", "(": ")"}

    def isValid(self, s: str) -> bool:
        if not len(s):
            return True
        i = 1
        for bracket in s:
            try:
                target = self.pairs[bracket]
                if s[i] == target:
                    new_string = s[0:i-1] + s[i+1::]
                    return self.isValid(new_string)
                i += 1
            except:
                i += 1
        return False
