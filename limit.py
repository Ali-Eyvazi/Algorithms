def limit():
   
   a=input('enter your array').split(" ")
   array=[]
   for i in a:
      array.append(int(i))
   min=int(input('enter your minimum number'))
   max=int(input('enter your maximum number'))

   min_check = lambda val : True if min is None else (val>=min)
   max_check = lambda val : True if max is None else (val<=max)

   return [ val for val in array if min_check(val) and max_check(val)]

print(limit())














