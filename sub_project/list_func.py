# here a user will input a list of there choice which will later have some changes.
import numpy as np 

data_entry = int(input("Enter numbers separated by spaces.: "))

numbers= [int(num) for numm in data_entry.split()]

array= np.array(array)
array_sum = np.sum(array)

array_sub = np.sub(array)

print(f"the sum of the numbers is: {array_sum}")
print(f"the sub of the numbers is: {array_sub}")

print("Thank you for using this small application.")