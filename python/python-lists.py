#!/usr/bin/env python3

# lists are an organized collection of items (integers, strings, etc) in square brackets, and are comma-separated
# lists can have duplicate values
lista = ['one', 'two', 3, 4, 'five']
listb = ['six', 'seven', 'eight', 9, 10, 'eleven', 'eleven', 'eleven']

print('\n'+'='*30)
print('\ntwo whole lists in raw form (one with duplicated values)')
print(lista)
print(listb)

print('\nmaking a unique list via list(set())')
print(list(set(listb)))

print('\naccess each item in the list with a "for" statement')
for i in lista:
	print(i)

# access the list by "slicing" it via index
# indexes start at 0, not 1 - ex. the first item in lista, "one", has an index of zero
# [start_index:stop_count:step] - start_index is an INDEX, stop_count as a literal COUNTING of items, not indexes, step is every item to be processed (default every item)
# start index position does not require colon usage
print('\n'+'='*30)
print('\nfirst item')
print(lista[0])

print('\neverything until the 4th position (one, two, 3, 4)')
print(lista[:4])

print('\nonly the 2nd through 4th positions (two, 3, 4)')
print(lista[1:4])

print('\nevery 2nd item')
print(lista[::2])

print('\nlist in reverse')
print(lista[::-1])

# joining lists becomes useful when displaying outputs, or creating formatted data for other functions and/or external programs
print('\n'+'='*30)
print('\njoin two string-type items with a space')
print(' '.join(lista[0:2]))

print('\nforce-convert all mixed-type items to string-type via generator, and join with a space')
print(' '.join(str(x) for x in lista))

print('\nforce a mapping of all mixed-type items in a list to string-type, and join with a space')
print(' '.join(map(str, lista)))

# lists can be merged, appended, and extended
print('\n'+'='*30)
print('\nintroducing a second list to the first one')
print(listb)

print('\nconcatenate two lists')
listadd = lista+listb
print(listadd)

print('\nconcatenate two lists with only unique values')
listuni = list(set(lista+listb))
print(listuni)

print('\nappend the old list to the new one')
listc = lista
for i in listb:
	listc.append(i)
print(listc)

print('\nextend the old list to the new one')
listd = lista
for i in listb:
	listd.extend(str(i))
print(listd)

print()

'''
==============================

two whole lists in raw form (one with duplicated values)
['one', 'two', 3, 4, 'five']
['six', 'seven', 'eight', 9, 10, 'eleven', 'eleven', 'eleven']

making a unique list via list(set())
[9, 10, 'six', 'eight', 'seven', 'eleven']

access each item in the list with a "for" statement
one
two
3
4
five

==============================

first item
one

everything until the 4th position (one, two, 3, 4)
['one', 'two', 3, 4]

only the 2nd through 4th positions (two, 3, 4)
['two', 3, 4]

every 2nd item
['one', 3, 'five']

list in reverse
['five', 4, 3, 'two', 'one']

==============================

join two string-type items with a space
one two

force-convert all mixed-type items to string-type via generator, and join with a space
one two 3 4 five

force a mapping of all mixed-type items in a list to string-type, and join with a space
one two 3 4 five

==============================

introducing a second list to the first one
['six', 'seven', 'eight', 9, 10, 'eleven', 'eleven', 'eleven']

concatenate two lists
['one', 'two', 3, 4, 'five', 'six', 'seven', 'eight', 9, 10, 'eleven', 'eleven', 'eleven']

concatenate two lists with only unique values
['two', 'five', 3, 4, 9, 'six', 10, 'one', 'seven', 'eight', 'eleven']

append the old list to the new one
['one', 'two', 3, 4, 'five', 'six', 'seven', 'eight', 9, 10, 'eleven', 'eleven', 'eleven']

extend the old list to the new one
['one', 'two', 3, 4, 'five', 'six', 'seven', 'eight', 9, 10, 'eleven', 'eleven', 'eleven', 's', 'i', 'x', 's', 'e', 'v', 'e', 'n', 'e', 'i', 'g', 'h', 't', '9', '1', '0', 'e', 'l', 'e', 'v', 'e', 'n', 'e', 'l', 'e', 'v', 'e', 'n', 'e', 'l', 'e', 'v', 'e', 'n']
'''
