class Solution:
    def plusOne(self, digits: 'List[int]') -> 'List[int]':
        up = 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                up = 0
                break
        if up == 1:
            digits.insert(0, 1)
        return digits


if __name__ == '__main__':
    x = Solution().plusOne([9, 9, 9, 9])
    print(x)
