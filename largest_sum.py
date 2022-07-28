
def large_sum(File_path : str)-> int:

    with open(File_path,'r') as f:
                Imported_file=list(f.read())
    stck=[]
    numbers=[]
    result=0
    for _ in range(100):
        for _ in range (50):
            b=Imported_file.pop(0)
            stck.append(b)
        numbers.append(stck)
        stck=[]
    for h in range(100):
        s=''.join(numbers[h])
        result+=int(s)
        
    return result

print(large_sum('larg_sum.txt'))