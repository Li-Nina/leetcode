#!/usr/bin/env python
# -*- coding:utf-8 -*-


class MinHeap:
    def __init__(self, _list=None):
        self.h = _list if _list else []
        self.h.insert(0, None)
        self.heapify()

    def heapify(self):
        pass

    def append(self, val):
        self.h.append(val)
        cur = len(self.h) - 1
        parent = cur // 2
        while parent > 0 and self.h[parent] > self.h[cur]:
            self.swap(cur, parent)
            cur = parent
            parent = cur // 2

    def pop(self):
        self.swap(1, -1)
        min_val = self.h.pop()
        cur = 1
        child = 2 * cur
        while child < len(self.h) and self.h[cur] > self.h[child]:
            self.swap(cur, child)
            cur = child
            child = 2 * cur
        return min_val

    def delete(self, index):


    def swap(self, cur, parent):
        temp = self.h[cur]
        self.h[cur] = self.h[parent]
        self.h[parent] = temp


if __name__ == '__main__':
    print(3 // 2)
    print(1 // 2)
