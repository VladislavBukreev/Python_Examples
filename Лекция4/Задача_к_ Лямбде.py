# 1. В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38,1444)]

# ОБЫЧНЫЙ МЕТОД

# spisok = [1 , 2 , 3 , 5 , 8 , 15 , 23 , 28]
# res = list()

# for i in spisok:
#     if i % 2 == 0:
#         res.append((i, i**2))

# print(res)


# ХОРОШИЙ МЕТОД

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# spisok = [1 , 2 , 3 , 5 , 8 , 15 , 23 , 28]

# res = select(int, spisok) #
# print(res)

# res = where(lambda x: x % 2 == 0, res)
# print(res)

# res = list(select(lambda x: (x, x**2), res))
# print(res)



#Лучший метод
spisok = [1 , 2 , 3 , 5 , 8 , 15 , 23 , 28]

res = map(int, spisok) 
print(res)

res = filter(lambda x: x % 2 == 0, res)
print(res)

res = list(map(lambda x: (x, x**2), res))
print(res)


