class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        while i >= 0:
            if digits[i] < 9:
                digits[i] += 1
                return digits
            if digits[i] == 9:
                if i == 0:
                    digits[i] = 0
                    result = [1]
                    result.extend(digits)
                    return result
                elif i != 0:
                    digits[i] = 0
                    i -= 1

        return digits


A = [9, 9]
print(Solution().plusOne(A))
