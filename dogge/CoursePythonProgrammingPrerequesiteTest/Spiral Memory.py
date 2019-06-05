import math


class Solution:
    def shortest_distance(self, target: int) -> int:
        def cal_level():
            return math.ceil((-1 + math.sqrt(target)) / 2)

        def cal_pivot_distance(level):
            below_level = level - 1
            level_start_num = 8 * ((below_level + 1) * below_level / 2) + 2
            step = 8 * level / 4
            return min([abs(target - (level_start_num + level - 1 + step * i)) for i in range(4)])

        if target <= 1:
            return 0
        lvl = cal_level()
        pivot_distance = cal_pivot_distance(lvl)
        return int(lvl + pivot_distance)


if __name__ == '__main__':
    print(Solution().shortest_distance(1))
    print(Solution().shortest_distance(12))
    print(Solution().shortest_distance(23))
    print(Solution().shortest_distance(1024))
    print("----------------------------------")
    print(Solution().shortest_distance(100000))
    print(Solution().shortest_distance(2345678))
