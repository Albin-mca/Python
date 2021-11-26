#31From a list of integers, create a list removing even numbers
a=[1,2,3,4,5,6,7,8,9,10]
print("Given List",a)
for i in a:
    if(i % 2==0):
        a.remove(i)
print(a)
