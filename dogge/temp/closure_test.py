def line_conf():
    b = 15

    def line(x):
        return 2 * x + b

    return line  # return a function object


b = 5
my_line = line_conf()
print(my_line.__closure__)
print(my_line.__closure__[0])
print(my_line.__closure__[0].cell_contents)


# print(my_line.__closure__[1].cell_contents)
