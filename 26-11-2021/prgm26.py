# 26.Create a string from given string where first and
# last characters exchanged. [eg: python - nythop]
k = str(input("Enter the String :"))
print("Entered string is :", k)

a = k[-1]
b = k[1:-1]
c = k[0]
d = a + b + c
print("Characters Exchanged:")
print(a + b + c)
