def reverse3(lst):
    for i in range(0, len(lst), 3): # loop through the list by 3
        lst[i:i+3] = lst[i:i+3][::-1] # reverse the 3 elements
    return lst # return the list

print(reverse3(['a' ,'b' , 'c', 'd', 'e', 'f', 'g', 'h'])) # print the result