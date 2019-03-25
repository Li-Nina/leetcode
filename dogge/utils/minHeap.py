#!/usr/bin/env python
# -*- coding:utf-8 -*-


class MinHeap:
    def __init__(self, _list=None, heapify='sink'):
        self.h = _list if _list else []
        if self.h:
            if heapify == 'sort':
                # 将list从小到大排序，构造最小堆
                self._heapify_sort()
            elif heapify == 'sink':
                # 从后往前遍历父节点，将不符合堆序性质的元素下沉
                self._heapify_sink()
        self._idx = 1

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.h[self._idx]
        except IndexError:
            self._idx = 1
            raise StopIteration()
        self._idx += 1
        return item

    def _heapify_sort(self):
        self.h.sort()
        self.h.insert(0, None)

    def _heapify_sink(self):
        self.h.insert(0, None)
        first_parent = (len(self.h) - 1) // 2
        for index in range(first_parent, 0, -1):
            self._sink(index)

    def _sink(self, index):
        # 将index处的元素按堆序性质下沉,制造空穴，开始下沉
        # 此方法用于pop树顶和构造堆
        num = self.h[index]
        length = len(self.h)
        lchild = 2 * index
        while lchild < length:
            if lchild + 1 < length and self.h[lchild + 1] < self.h[lchild] and self.h[lchild + 1] < num:
                self.h[index] = self.h[lchild + 1]
                index = lchild + 1
            elif self.h[lchild] < num:
                self.h[index] = self.h[lchild]
                index = lchild
            else:
                break
            lchild = 2 * index
        self.h[index] = num

    def _swim(self, index):
        # 将index处的元素按堆序性质上浮,制造空穴，开始上浮。
        # 此方法只用于往堆中插入新元素
        num = self.h[index]
        parent = index // 2
        while parent > 0 and self.h[parent] > num:
            self.h[index] = self.h[parent]
            index = parent
            parent = index // 2
        self.h[index] = num

    def _swap(self, cur, parent):
        temp = self.h[cur]
        self.h[cur] = self.h[parent]
        self.h[parent] = temp

    def append(self, val):
        self.h.append(val)
        cur = len(self.h) - 1
        self._swim(cur)

    def pop(self):
        self._swap(1, -1)
        min_val = self.h.pop()
        if len(self.h) > 1:
            self._sink(1)
        return min_val

    def is_empty(self):
        return len(self.h) == 1


if __name__ == '__main__':
    h = MinHeap(_list=[6, 8, 9, 3, 2, 1, 4, 5, 7, 0, 1, 11, 9, 8], heapify='sink')
    for i in h:
        print(i, end=' ')
    print()
    h.append(4)
    h.append(9)
    h.append(8)
    h.append(7)
    h.append(9)
    h.append(0)
    h.append(-7)
    h.append(-5)
    h.append(11.2)
    for i in h:
        print(i, end=' ')
    print()
    while not h.is_empty():
        x = h.pop()
        print("-->pop", x, end=' after ')
        for i in h:
            print(i, end=' ')
        print()
    for i in h:
        print(".....>", i)

    h.append(4)
    h.append(3)
    h.append(1)
    h.append(-9)
    h.append(8)
    h.append(7)
    h.append(1)
    h.append(4)
    h.append(4)
    h.append(4)
    h.append(4)
    for i in h:
        print(i, end=' ')
    print()
    while not h.is_empty():
        x = h.pop()
        print("-->pop", x, end=' after ')
        for i in h:
            print(i, end=' ')
        print()
    for i in h:
        print(".....>", i)
