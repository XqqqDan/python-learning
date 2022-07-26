def swap(a, b):
    a, b = b, a
    return (a, b)


a = input()
b = input()
a, b = swap(a, b)
print(a)
print(b)
