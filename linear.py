"""
        linear(sequential) search
            [1,2,5,8,11,14,18,23,32,48]  11=>4

"""

def linear_search(array : list,element : int)->int :
    for i in range(len(array)):
        if array[i] == element:
            return i

    return -1

print(linear_search( [1,2,5,8,11,14,18,23,32,48] , 11))







