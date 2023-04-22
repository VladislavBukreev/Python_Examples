# Словари
# Словари — неупорядоченные коллекции произвольных объектов с доступом по ключу.
# В списках в качестве ключа используется индекс элемента. В словаре для определения
# элемента используется значение ключа (строка, число).

dictionary = {}  #создание пустого словаря
d = dict()


dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}

print(dictionary['left']) # ← типы ключей могут отличаться
print(dictionary['up']) # ↑ типы ключей могут отличаться

dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐

print(dictionary['type']) # KeyError: 'type' такаго ключа нет




del dictionary['left'] # удаление элемента
for item in dictionary: # распечатает все ключи за исключением удалённого
     print(item)        #up
                        #down
                        #right

for item in dictionary: # распечатает все ключи и зачения к ним за исключением удалённого
    print('{}: {}'.format(item, dictionary[item]))  # up: ↑
                                                    # Down: ↓
                                                    # right: →

for (k,v) in dictionary.items():
     print(k,v)                                     # up: ↑
                                                    # Down: ↓
                                                    # right: →



print(dictionary.items())