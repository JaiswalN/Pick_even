def myfunc(*args):
   	list = []
    
	for value in args:
        
	if value%2 == 0:
            
	list.append(value)
    
	return list
    

print(myfunc(2,4,5,6,7,8,9))