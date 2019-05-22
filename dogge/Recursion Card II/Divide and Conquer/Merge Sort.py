class Solution:
    def sortArray_recursion(self, nums: 'List[int]') -> 'List[int]':
        if len(nums) <= 1:
            return nums
        left = self.sortArray_recursion(nums[0:len(nums) // 2])
        right = self.sortArray_recursion(nums[len(nums) // 2:])
        return self.merge(left, right)

    def sortArray_iteration(self, nums: 'List[int]') -> 'List[int]':
        nums_list = [[_] for _ in nums]
        while len(nums_list) != 1:
            if len(nums_list) % 2 != 0:
                nums_list.append([])
            length = len(nums_list)
            i = 0
            while i < length:
                nums_list.append(self.merge(nums_list[i], nums_list[i + 1]))
                i += 2
            nums_list = nums_list[length:]
        return nums_list[0]

    def merge(self, l1: 'List[int]', l2: 'List[int]'):
        rst = []
        p1 = p2 = 0
        if l1 and l2:
            while p1 < len(l1) and p2 < len(l2):
                if l1[p1] <= l2[p2]:
                    rst.append(l1[p1])
                    p1 += 1
                else:
                    rst.append(l2[p2])
                    p2 += 1
        rst.extend(l1[p1:])
        rst.extend(l2[p2:])
        return rst


if __name__ == '__main__':
    x = Solution().sortArray_recursion([1, 6, 4, 3, 8, 6, 2, 5, 0, 9, 9, 6])
    print(x)
    y = Solution().sortArray_iteration([1, 6, 4, 3, 8, 6, 2, 5, 0, 9, 9, 6])
    print(y)
