# def hello(name):
#     return f"Hi, {name}"

# def bye(name):
#     return f"{name}, bye-bye"

# def make_phrase(func):
#     name = input("Введите свое имя ")
#     print(func(name))

# def make_dialog(list_funcs):
#     res = ""
#     name = input("Введите свое имя ")
#     for func in list_funcs:
#         res += func(name) + "\n"
#     print(res)



# # make_phrase(hello)
# # make_phrase(bye)
# # name = input("Введите свое имя ")
# # print(hello(name))
# # print(bye(name))
# # lf = [hello, bye]
# # make_dialog(lf)

# # создадим ФВП которая может любое число возвести в любую степень
# def calc(degree):
#     def power(base):
#         return base ** degree
#     return power

# # print(calc(3)(2))

# # get_cube = calc(3)
# # get_square = calc(2)
# # print(get_cube(5))
# # print(get_square(5))

# # sq = lambda x: x ** 2
# # print(sq(7))
# # print(sq(9))
# # is_even = lambda x: True if x % 2 == 0 else False
# # is_even = lambda x: x % 2 == 0
# # print(is_even(2))
# # print(is_even(3))
# # calc = {
# #     "+": lambda x,y: x + y,
# #     "-": lambda x,y: x - y,
# #     "/": lambda x,y: x / y,
# #     "*": lambda x,y: x * y,
# #         }

# # eq = input("Введите арифметическое выражение ")
# # num1, op, num2 = eq.split()
# # print(calc[op](int(num1), int(num2)))
# sp = [1,2,3,4,5,6,8,99,11]
# # print(*map(lambda x: x ** 2, sp))
# # print(list(map(lambda x: x ** 2, sp)))
# # print(list(filter(lambda x: x % 2, sp)))
# for i, value in enumerate(sp):
#     print(f"{i = } , {value = }")

# sp2 = ["Vsya", "Sasha"]
# for item in zip(sp2, sp):
#     print(item)