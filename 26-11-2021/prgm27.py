# 27. Create a list of colors from comma-separated color
# names entered by user. Display first and last colors.
a = input("Enter the colors in comma-separated form :\n")
list1 = a.split(",")
print(list1)
print("First color in list", list1[0])
print("Last color in the list", list1[-1])
