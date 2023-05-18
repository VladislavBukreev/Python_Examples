def calk2(a, b):
    return a * b

def math(op, x, y):
     print(op(x, y))



# def calkl(a,b): 
#     return a + b                    # <- Это

calkl = lambda a,b: a + b           # <- Равносильно этому

math(calkl, 5, 45)
# ИЛИ ТАК
# math(lambda a,b: a+b, 5, 45)