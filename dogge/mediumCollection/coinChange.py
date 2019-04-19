class Solution:
    def coinChange(self, coins: 'List[int]', amount: int) -> int:
        memo = {}

        def coin_change(need_amount):
            if need_amount == 0:
                return 0
            elif need_amount < 0:
                return -1
            elif memo.get(need_amount):
                return memo[need_amount]
            else:
                rst = -1
                for i in coins:
                    n = coin_change(need_amount - i)
                    if n >= 0:
                        nums = n + 1
                    else:
                        nums = -1
                    if rst == -1 or 0 < nums < rst:
                        rst = nums
                memo[need_amount] = rst
                return rst

        return coin_change(amount)


if __name__ == '__main__':
    x = Solution().coinChange([388, 232, 419, 338, 49, 434, 4, 143], 4993)
    # x = Solution().coinChange([2], 4)
    print(x)
