# Кортежи
# Кортеж — это неизменяемый список.
t = () # создание пустого кортежа
print(type(t)) # class <'tuple'>
t = (1,)
print(type(t)) # class <'tuple'>
t = (1) 
print(type(t)) # class <'int'>
t = (28, 9, 1990)
print(type(t))



v = [1, 8, 9] 
print(v)  #[1, 8, 9]
print(type(v)) # <class 'list'>

v = tuple(v) 
print(v) (1, 8, 9)
print(type(v)) # <class 'tuple'>


a,b,c = v # можно присвоить сразу несколько переменных разом. 

print(a, b, c)




# Печатание кортежа
t = (1, 2, 3, 5,)
for i in t:
    print(i)
 
# равносильно следующему:

for i in range(len(t)):
    print(t[i])

