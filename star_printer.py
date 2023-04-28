#Factorial using recursion
def fact(n):
    if n<=1:
     return 1
    else :
     x = n * fact(n-1)
     return x


def printFun(test):

	if (test < 1):
		return
	else:

		print(test, end=" ")
		printFun(test-1) # statement 2
		print(test, end=" ")
		return


#Fibbonnaci using recursion
def fib(n):
    if(n == 0):
        return 0
    if (n == 1) or (n==2):
        return  1
    else:
        result = (fib(n-1) + fib(n-2))
        return result
    
def fact(n):
    if n<=1:
     return 1
    else :
     x = n * fact(n-1)
     return x


def star_printer1(n):
    for x in range(0,n):
        for y in range(0,n-x-1):
            print(' ',end=" ")
        for y in range(0,2*x+1):
            print('*',end=" ")
        for y in range(0,n-x-1):
            print(' ',end=" ")
        print("\n")

def star_printer2():
    for row in range(0,n):
        for column in range(0,row):
            print(" ",end=" ")
        for column in range(0,):
            print("*",end=" ")
        for column in range(0,row):
            print(" ",end=" ")
        print("\n")

def star_printer3(n):
    for x in range(1,n+1):
        for y in range(1,n+1):
            print('*',end=" ")

def star_printer4(n):
    for row in range(1,n+1):
        for column in range(1,row+1):
            print('*',end=" ")
        print("\n")    

        print()


def star_printer5(n):
    for row in range(1,n+1):
        for column in range(1,row+1):
            print(column,end=" ")
        print("\n")


def star_printer6(n):
    for row in range(0,n+1):
        for column in range(0,n-row+1):
            print('*',end=' ')
        print('\n')


def star_printer7(n):
    for row in range(1,n+1):
        for column in range(1,n-row+1):
            print(column,end=' ')
        print('\n')


def star_printer8(n):
    for r in range(0,n):
        for s in range(0,(n-r+1)):
            print(' ',end=' ')
        for c in range(0,(2*r+1)):
            print('*',end=' ')
        for s in range(0,(n-r+1)):
            print(' ',end=' ') 
        print('\n')

def star_printer9(n):
    for r in range(0,n):
        for s in range(0,r):
            print(" ",end=' ')
        for c in range(0,2*n-(2*r+1)):
            print('*',end=' ')
        for s in range(0,r):
            print(" ",end=' ')
        print('\n')

def star_printer10(n):
   for r in range(0,n):
      for s in range(0,n-r+1):
         print(" ",end="")
      for c in range(0,2*r+1):
         print("*",end="")
      for s in range(0,n-r+1):
         print(" ",end="")
      print()

def star_printer11(n):
   for r in range(0,n):
      for s in range(0,r):
         print(" ",end="")
      for c in range(0,2*n-(2*r+1)):
         print("*",end="")
      print()

def star_printer12(n):
   for r in range(0,2*n+1):
      stars =r
      if (stars>n): stars=2*n-r
      for c in range(0,stars):
         print("*",end="")
      print()

def star_printer13(n):
   for r in range(0,n):
       if (r%2 == 0): 
          start=1
       else: 
          start=0
       for c in range(1,r):
         print(start,end='')  
         start=1-start    
       print()


def printer(number_of_times):
    count=0
    while count<number_of_times:
        print("Am the guy.")
        count+=1

def Triangle(n):
    # Write your code here.
    for row in range(0,n+1):
        for space in range(0,row):
            print(" ",end="")
        for column in range(0,2*n-(2*row+1)):
            print("*",end="")
        for space in range(0,row):
            print(" ",end='')
        print('\n')
