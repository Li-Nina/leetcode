class A:
    def max(self):
        c = 0
        c1 = 3
        c2 = 4

        def line(x):
            return 2 * x + c + c1 + c2

        return line


class B:
    def haha(self):
        print A().max().__closure__[0].cell_contents
        print A().max().__closure__[1].cell_contents
        print A().max().__closure__[2].cell_contents


B().haha()
