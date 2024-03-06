#this is a simple application taking user input to create a bar graph
import matplotlib.pyplot as plt
import numpy as np

print("let your catergory be in uppercase. eg A B C ")

categories = input("Enter categories separated by spaces: ").upper().split()
values = list(map(int, input("Enter corresponding values separated by spaces: ").split()))

plt.bar(categories, values, color=['yellow','red'])
plt.xlabel('Categories')
plt.ylabel('Values')
print("This in uppercase as well. eg MY GRAPH")
plt.title(input("Enter the title of your bar graph.: ").upper())
plt.grid(axis='y')

plt.show()
print("Thank you for using this small application.")