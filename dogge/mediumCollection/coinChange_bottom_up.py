class Solution:
    def coinChange(self, coins: 'List[int]', amount: int) -> int:
        rst = [amount + 1 for _ in range(amount + 1)]
        rst[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                sub_pro = i - coin
                if sub_pro >= 0 and rst[sub_pro] + 1 < rst[i]:
                    rst[i] = rst[sub_pro] + 1
        return rst[amount] if rst[amount] < amount + 1 else -1


if __name__ == '__main__':
    x = Solution().coinChange([2], 3)
    print(x)
