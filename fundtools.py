from functools import reduce

def data(x,y):
    return x + y

def data2(a,b):
    return a * b

num=[1,2,3,4,5,6,7,8,9,10]

print(f"Reduce function for addition data: {reduce(data,num)}")
print(f"Reduce function for multiplication data: {reduce(data2,num)}")