#create a list of the first n numbers of the fibonacci series
counter = 0
num = 0
n = 20
fibonacci = []
while counter <= n:
    if len(fibonacci) == 0:
        fibonacci.append(num)
        counter += 1
    elif len(fibonacci) in (1,2):
        fibonacci.append(1)
    else:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
        counter += 1

        
