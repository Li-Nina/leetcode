class Solution:
    def reverseString(self, s: 'List[str]') -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def swap(i, j):
            if i < j:
                s[i], s[j] = s[j], s[i]
                swap(i + 1, j - 1)

        swap(0, len(s) - 1)


if __name__ == '__main__':
    x = [1, 2, 3, 4, 5]
    Solution().reverseString(x)
    print(x)
