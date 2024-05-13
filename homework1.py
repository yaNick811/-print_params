def print_parasma(a = 1, b = 'слово', c = True):
    print(a, b, c)


print_parasma()
print_parasma(10, 'новая строка')
print_parasma(b= 25)
print_parasma(c = [1,2,3])


values_list = [21, 'text', True]
values_dict = {'a': 5, 'b': 'slova', 'c':True}
print_parasma(*values_list)
print_parasma(**values_dict)


values_list2 = [18, 'Hola']
print_parasma(*values_list2, 42)
