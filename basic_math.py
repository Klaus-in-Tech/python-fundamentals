from math import log

def calculate_digits(N):
    digit_count = int(log(N)+1)
    print(digit_count)


def reverse_number(N):
    global new_reversed_number
    new_reversed_number=0
    while (N>0):
        last_digit=N%10
        N=int(N/10)
        new_reversed_number = (new_reversed_number*10)+last_digit
    print(new_reversed_number)


def palindrome(N):
    dup=N
    new_reversed_number=0
    while (N>0):
        last_digit=N%10
        N=int(N/10)
        new_reversed_number = (new_reversed_number*10)+last_digit
    if dup == new_reversed_number :
        print('True')
    else:
        print('False')

def armstrong(N):
    dup=N
    sum=0
    while N>0:
        last_digit=N%10
        N=int(N/10)
        sum=sum+(last_digit**3)
    if sum==dup:
        print('True')
    else:
        print("False")

def multiples(N):
    dup=N
    my_list=[]
    for x in range(1,N+1):
        if (dup%x == 0):
            my_list.append(x)
            x+=1
        else:
            x+=1
    print(my_list)
        
def prime_numbers(N):
    for x in range(1,N):
        if N%x == 0:
            print(x)
        else: 
            print(N)
            break

prime_numbers(4)