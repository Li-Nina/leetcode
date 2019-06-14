class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """

    def twoSum(self, numbers, target):
        # write your code here
        vi_dict = {v: i for i, v in enumerate(numbers)}
        for i, v in enumerate(numbers):
            if target - v in vi_dict:
                return [vi_dict[target - v], i] if vi_dict[target - v] < i else [i, vi_dict[target - v]]
