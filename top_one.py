def top(array):
    values={}
    f_val=0
    result=[]

    for i in array:
        if i in values:
            values[i]+=1
        else:
            values[i]=1


    f_val=max(values.values())
    

    for i in values.keys():
        if values[i]==f_val:
            result.append(i)
        else:
            continue

    return result , f_val


print(top([1,2,1,3,4,5]))
    