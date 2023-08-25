def partition(x):
    if(x % 2 == 0):
        t = (x,'none')
    else:
        t = ('none', x)
        return t
    

def partition_list(list):
    new_list =[]
    for i in list:
        new_list.append(partition(i))
    return new_list

print (partition([1,2,3,4,5,6,7,8,9,10]))