import math 
number = int(input())
answer = 0
while number >0:
    x = number % 10
    number = number // 10
    answer = answer * 10
    answer = answer + x
    print (answer)