
'''Write a Python program to sum three given integers. However, if two or more values are
equal sum will be zero.'''

def sum(x, y, z):
    if x == y or y == z or x==z:
        sum = 0
    else:
        sum = x + y + z
    return sum

print(sum(7, 1, 2))
print(sum(4, 2, 2))
print(sum(5, 2, 2))
print(sum(2, 4, 3))