#!/usr/bin/env python

# function definition for reverse of a number

def reverse(n):
    reminder = 0
    rev = 0
    while (n > 0):
        reminder = n % 10
        n = int(n / 10)
        rev = reminder + (rev * 10)
    return rev
    
for _ in range(int(input())):
    n = int(input("Enter the number to be reversed : "))
    print("Reversed Number : ", reverse(n))
