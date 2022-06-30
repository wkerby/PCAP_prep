print([i for i,x in enumerate(list(range(6+1)))])
def factorial(x):
    mult_list = []
    for i,z in enumerate(list(range(x+1))):
        if i > 0:
            mult_list.append(z)
        product = 1
        for i in list(range(len(mult_list)-1)):
            product = product*mult_list[i+1]
    return print(product)
factorial(6)
            
            
                         
    
