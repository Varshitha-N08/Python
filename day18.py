# a={"a":1,"b":2,"c":3}
# b={"d":5,"f":6}
# a.update(b)
# print(a)

# a={"a":1,"b":2,"c":3}
# b={"d":5,"f":6}
# b.update(a)
# print(b)

# a={"a":1,"b":2,"c":3}
# x=a.pop("c")
#  print(x)

# a={"a":1,"b":2,"c":3}
# del a["c"]
# print(a)

a={"a":1,"b":2,"c":3}
x=a.pop("c")
print(x)

a={"a":1,"b":2,"c":3}
a.popitem()
print(a)

a={"a":1,"b":2,"c":3}
a.clear()
print(a)