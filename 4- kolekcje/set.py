# 1. Utwórz dowolną krotkę, w której elementy mogą się powtarzać. Przekształć ją w set.

fruit_tuple = ('jabłko', 'arbuz', 'cytryna')
fruit_set = set(fruit_tuple)
print(fruit_set)

# 2. Utwórz listę L_test = [1, 2, 3, 4], krotkę T_test = (1, 2, 3, 4) oraz set S_test = {1, 2, 3, 4}.
# Jakie metody dostępne dla typu list nie będą działać dla typów tuple i set?

L_test = [1, 2, 3, 4]
T_test = (1, 2, 3, 4)
S_test = {1, 2, 3, 4}

"""
list vs set
Na set nie działa:
append()	
count()
extend()
index()
insert()
reverse()
sort()


list vs tuple
Na tuple  nie działą:
append()
clear()
copy()
extend()
insert()
pop()
remove()
reverse()
sort()
"""


# 3. Utwórz 2 krotki.  Następnie utwórz listę będącą połączeniem elementów o parzystym indeksie z pierwszej krotki,
# a oraz nieparzystych elementów z drugiej.
# Przekształć powstałą listę w set.

one_tuple = (1, 2, 3, 4)
two_tuple = ('a', 'b', 'c', 'd')

one_list = list(one_tuple[::2])
print(one_list)
two_list = list(two_tuple[1::2])
print(two_list)

list_all = one_list + two_list
print(list_all)
set_all = set(one_list + two_list)
print(set_all)

# 4. Napisz skrypt, który podaną listę podzieli na 3 równe listy i odwraca każdą z tych.
#
#     input: [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
#
#     output:
#
#     [4, 3, 2, 1]
#     [14, 13, 12, 11]
#     [24, 23, 22, 21]

start_list = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
third = len(start_list) // 3
list_1 = start_list[0: third]
list_2 = start_list[third: -third]
list_3 = start_list[-third::]

list_1.reverse()
list_2.reverse()
list_3.reverse()

print(list_1)
print(list_2)
print(list_3)

# 5  Porównaj zachowanie discard() vs remove() dla typu set.

# The discard() method removes the specified item from the set.
# The remove() method removes the specified element from the set.

# The discard() method is different from the remove() method,
# because the remove() method will raise an error if the specified item does not exist,
# and the discard() method will not.

colours = {"blue", "orange", "red"}
colours.discard("green")
print(colours)
