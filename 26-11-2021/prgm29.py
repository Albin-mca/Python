# 29.Create a single string separated with space from
# two strings by swapping the character at position 1
a = "Cute"
b = "Girl"
c = a[0]
d = b[-1]
print(c, d, "\n")

e = a[1:]
f = b[:-1]
print(e, f, "\n")

g = d + e
h = f + e
print("Character after swapping")
print(g + " " + h)
