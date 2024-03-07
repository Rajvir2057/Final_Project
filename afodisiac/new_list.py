import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


names= []
ages= []
dob = []

for filename in os.listdir('.'):
    if filename.endswith('.txt'):
        with open(filename,'r') as file:
            lines = file.readlines()
            name = lines[0].split(':')[1].strip()
            age = int(lines[1].split(':')[1].strip())
            year = lines[2].split(':')[1].strip()

            names.append(name)
            ages.append(age)
            dob.append(year)

data= {'Names': names, 'Ages': ages, 'dob': dob}
print(data)
def add_one(x):
    return x+1
values_for_ages = data['Ages']
added_val =map(add_one,values_for_ages)
added_val_list = list(added_val)
print(f"next year these are the ages of our users: {added_val_list}")
df = pd.DataFrame(data)
ages_list = data['Ages']
print(f" ages list is: {ages_list}")
# next_years_age = map(lambda x: x+1, ages_list)
# print(next_years_age)
# age_array = np.array(ages_list)
# mean_age = np.mean(age_array)
# print(mean_age)

# name_list = data['Names']s
# print(name_list)
# plt.bar(name_list,ages_list,color='blue')
# plt.xlabel("names")
# plt.ylabel('age')
# plt.title('A bar graph')
# plt.grid(axis='y')
# plt.show()

# def func():
    # data= {'Names': names, 'Ages': ages, 'dob': dob}
    # print(data)
    # val_ages = data["Ages"]
    # next_years_age = lambda val_ages: val_ages+1
    # print()


