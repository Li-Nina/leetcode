class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        right = 0
        while x > right:
            right = right * 10 + x % 10
            x //= 10
        return x == right or x == right // 10


if __name__ == '__main__':
    print(Solution().isPalindrome(0))
