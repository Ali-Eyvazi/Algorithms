inputs=[]
n = int(input())
for i in range (n):
    str = input().split(" ")
    inputs.append(str)
print (inputs)


for i in range (n):
        if int(inputs[i][2])==1:
            a=int(inputs[i][0])
        elif (int(inputs[i][0])/(int(inputs[i][2])+1))>2:
            a=int(inputs[i][0])/(int(inputs[i][2])+1)

        elif (int(inputs[i][0])/int(inputs[i][2]))<=2 and (int(inputs[i][0])/int(inputs[i][2]))<1.5 :
            a=(int(inputs[i][0])/int(inputs[i][2]))+1

        else:
            a=1


        if int(inputs[i][3])==1:
            b=int(inputs[i][1])
        elif (int(inputs[i][1])/(int(inputs[i][3])+1))>2:
            b=int(inputs[i][1])/(int(inputs[i][2])+1)

        elif (int(inputs[i][1])/(int(inputs[i][3])))<=2 and (int(inputs[i][1])/int(inputs[i][3]))<1.5:
                b=(int(inputs[i][1])/int(inputs[i][3]))+1
        else:
            b=1
        print (a)
        print (b)
        print(int(a)*int(b))