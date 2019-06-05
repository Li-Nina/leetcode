class Solution:
    def finding(self, target: int):
        def backtracking(factors: 'List[int]', sub_target: int):
            if sub_target == 1:
                return tuple(factors)
            rst = sub_target_try(factors, sub_target, 2)
            if rst:
                return rst
            rst = sub_target_try(factors, sub_target, 3)
            if rst:
                return rst
            rst = sub_target_try(factors, sub_target, 5)
            if rst:
                return rst

        def sub_target_try(factors: 'List[int]', sub_target: int, try_num: int):
            if sub_target % try_num == 0:
                factors.append(try_num)
                rst = backtracking(factors, sub_target // try_num)
                if rst:
                    return rst
                factors.pop()

        return backtracking([], target) if target > 1 else None


if __name__ == '__main__':
    print(Solution().finding(1))
    print(Solution().finding(6))
    print(Solution().finding(8))
    print(Solution().finding(14))
    print("---------------------")
    print(Solution().finding(1845281250))
    print(Solution().finding(3690562500))
    print(Solution().finding(1230187500))
    print(Solution().finding(10023750))
