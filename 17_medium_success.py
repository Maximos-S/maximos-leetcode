class Solution:

    def __init__(self):
        self.number_dict = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return [char for char in self.number_dict[digits[0]]]
        res_list = self.letterCombinations(digits[1:])
        new_res_list = []
        for char in self.number_dict[digits[0]]:
            self.letterHelper(char, res_list, new_res_list)
        return new_res_list

    def letterHelper(self, char, str_list, new_res_list):
        for string in str_list:
            new_res_list.append(f"{char}{string}")
