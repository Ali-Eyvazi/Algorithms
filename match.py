
out=[]
details=[]
result=[]
matches = int(input())
for i in range(matches):
    details.append( input().split(" "))

    
    match=details.pop(0) 
    first_team=int(match[0])+int(match[2])
    second_team=int(match[1])+int(match[3])

  
    if first_team > second_team :
        result.append('perspolis')
    elif second_team > first_team  :
        result.append('esteghlal')
        
    elif first_team == second_team :
        if ((int(match[0]) > int(match[1])) or int(match[2]) > int(match[3]))and (int(match[2]) > int(match[1])) :
            result.append('perspolis')
        elif ((int(match[1]) > int(match[0])) or int(match[3]) > int(match[2]))and (int(match[1]) > int(match[2])):
            result.append('esteghlal')
        else:
            result.append('penalty')



    first_team=0
    second_team=0
for i in result:
    print(i)
