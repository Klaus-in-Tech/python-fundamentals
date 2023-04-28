user_input = int(input('Enter your desired number of FizzBuzzes: '))

count= 0
number= 1
my_numbers = []
while count != user_input:
    if (number % 3 == 0) and (number % 5 == 0):
        my_numbers.append("FizzBuzz")
        count +=1
    elif (number % 3 == 0):
        my_numbers.append("Fizz")
    elif(number % 5 == 0): 
        my_numbers.append("Buzz")
    else:
        my_numbers.append(number)
    number += 1

for i in range(0,len(my_numbers)):
    if my_numbers[i] == my_numbers[-1]:
        print(my_numbers[i])
    elif my_numbers[i+1] == 'FizzBuzz':
        print(my_numbers[i])
    elif my_numbers[i] == 'FizzBuzz':
        print(my_numbers[i])
    else:
        print(my_numbers[i],end=',') 

    
