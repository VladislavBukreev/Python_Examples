# МНОЖЕСТВА
# Множества содержат в себе уникальные элементы, не обязательно упорядоченные.
# Одно множество может содержать значения любых типов. Если у Вас есть два множества,
# Вы можете совершать над ними любые стандартные операции, например, объединение,
# пересечение и разность. Давайте разберем их.


colors = {'red', 'green', 'blue'} # Создание множества
# Или так 
q = set({'red', 'green', 'blue'})
print(colors) # {'red', 'green', 'blue'}
# или
print(q) #{'red', 'green', 'blue'}

# .add  - добавление значение в множестве
colors.add('red') 
print(colors) # {'red', 'green', 'blue'}
colors.add('gray')
print(colors) # {'red', 'gray', 'green', 'blue'}

# .remove -  удаление значения в множестве
colors.remove('red')
print(colors) # {'green', 'blue','gray'}
colors.remove('red') # KeyError: 'red' (уже удалили)

colors.discard('red') # Удаление значения в множестве если оно есть, если его нет просто пропускает

colors.clear() #{} Удаление всех элементов в множестве


# ОПЕРАЦИИ СО МНОЖЕСТВАМИ В PYTHON
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()                # c = {1, 2, 3, 5, 8}
u = a.union(b)              # u = {1, 2, 3, 5, 8, 13,
i = a.intersection(b)       # i = {8, 2, 5}
dl = a.difference(b)        # dl = {1, 3}
dr = b.difference(a)        # dr = {13, 21}
q = a.union(b).difference(a.intersection(b))# {1, 21, 3, 13}



# ЗАМОРОЖЕННЫЕ МНОЖЕСТВА
# Неизменяемое или замороженное множество(frozenset) — множество, с которым не будут
# работать методы удаления и добавления.

a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b) # frozenset({1, 2, 3, 5, 8})
