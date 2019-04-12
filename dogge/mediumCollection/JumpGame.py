class Solution:
    """
    Input: [2,3,1,1,4]
    Output: true
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

    Input: [3,2,1,0,4]
    Output: false
    Explanation: You will always arrive at index 3 no matter what. Its maximum
                 jump length is 0, which makes it impossible to reach the last index.
    """

    def canJump(self, nums: 'List[int]') -> bool:
        n = set()

        def sub_jump(index):
            if index == 0:
                return True
            point = index
            step = 1
            index -= 1
            while index >= 0:
                if nums[index] >= step and index not in n:
                    if sub_jump(index):
                        return True
                step += 1
                index -= 1
            n.add(point)
            return False

        return sub_jump(len(nums) - 1)


def adjust_digit(num, digit, maximum=False):
    _place = 10 ** digit
    _up = 0.1 ** digit
    truncate = int(num * _place) / _place
    # maximum=True，求最大值，num已经是最大值，直接截取
    if not maximum:
        # maximum=False，求最小值，num已经是最小值，截取后在末尾+1
        truncate += _up
    return truncate


if __name__ == '__main__':
    a = [1,2]
    x = a.sort()
    print(x)