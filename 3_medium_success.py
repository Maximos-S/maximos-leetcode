class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest_substring = 0
        current_sub = ""
        for letter in s:
            if letter in current_sub:
                current_sub = current_sub[current_sub.index(
                    letter) + 1:] + letter
            else:
                current_sub = current_sub + letter

            if len(current_sub) > longest_substring:
                longest_substring = len(current_sub)

        return longest_substring
