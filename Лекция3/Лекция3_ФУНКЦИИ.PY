def sum_numbers(n):
    summa = 0
    for i in range(1, n+1):
        summa += i
    print(summa)

sum_numbers(5)  # 15

#################################

def sum_numbers(n):
    summa = 0
    for i in range(1, n+1):
        summa += i
    return summa
print(sum_numbers(5))  # 15

#################################

def sum_numbers(n, y ="Hello"):
    print(y)
    summa = 0
    for i in range(1, n+1):
        summa += i
    return summa
a = sum_numbers(5)
print(a)  # Hello
          # 15

################################
#НЕОГРАНИЧЕННЫЕ ПЕРЕМЕННЫЕ 

def sum_str(*args):
    res = ""
    for i in args:
        res += i
    return res

print(sum_str('q', 'e', 'l')) #qel
print(sum_str('q', 'e', 'l','r','f'))#qelrf
print(sum_str(8 , 9, 10)) # Ошибка