from array import *
def print_prime_numbers(number,data_array):
    for k in range(2,number,1):#This ensures that 1 and the number itself are not used in the loop
        if number%k==0:
            return
        else:
            pass
    else:
        if number!=1:
            data_array.append(number)
        else:
            pass

num=int(input("Input a number upto which you want to generate prime numbers"))
data=array('i',[])
data.append(2)#This is done to enable working of the next line
for i in range(1,num+1,2):#For optimization-to work with odd numbers only
    print_prime_numbers(i,data)
print("Prime numbers between 0 and ",num)
for j in data:
    print(j,end=" ")