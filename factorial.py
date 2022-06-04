# n! = 1 * 2 * 3 * 4 * ......* n 
# 3! =  3 * 2 * 1     => 6 

num = int(input('Enter  number :  '))

factorial = 1 
for i in range(1, num+1 ):
    # print(i)
    factorial = factorial* i 

print(factorial)

