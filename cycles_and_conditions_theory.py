# 1
print(not True)             # False
print(not False)            # True

# 2
cond1 = 0 < 1
cond2 = 1 < 4

print(cond1 and cond2)      # True
# 3
cond3 = 't' in 'Python'
cond4 = 'd' in 'Python'
print(type(cond3), cond3)   # <class 'bool'> True
print(cond3 and cond4)      # False

# 4
print(cond3 or cond4)       #True
print(not True or (True and not True))                  # False
print(not False and True or False and not True)         # True

# 5
a = [1, 2, 3]
b = a
print(a == b)   # True
print(a is b)   # True

c = [1, 2, 3]
d = [1, 2, 3]
print(c == d)   # True
print(c is d)   # False
