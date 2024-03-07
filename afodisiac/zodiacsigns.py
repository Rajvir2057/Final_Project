from abc import ABC,abstractclassmethod
import time
from datetime import datetime 
import matplotlib.pyplot as plt

import os
import pandas as pd
import numpy as np
current_drectory = os.getcwd()

class App:
    @abstractclassmethod
    def get_your_zodiac():
        pass

class Zodiac(App):

    def __init__(self,  month, day):
        
        self.month= month
        self.day= day
    
    def get_zodiac_signs(self):
        zodiac_signs = {
    "Aries": "unafraid of conflict, highly competitive, and honest",
    "Taurus": "Sensual,emotionally strong and hardworking,",
    "Gemini": "curious, clever, and outstanding communicators who are pretty unpredictable",
    "Cancer": "Nurturing and loyal",
    "Leo": "Generous, warmhearted, creative, enthusiastic, and faithful.",
    "Virgo": "diligent workers who excel at what they do, but their lofty ambitions can lead them to be too critical of others.",
    "Libra": "extroverted, cosy, and friendly people",
    "Scorpio": "strong, enigmatic and independent characters who crackle with an intensity and charisma that makes them un-ignorable.",
    "Sagittarius": "adventurers, risk-takers, and have a sharp business and sports mentality.",
    "Capricorn": "perfectionist, hardworking, and organised.",
    "Aquarius": " intellectual, thoughtful, charismatic, and an expert communicator.",
    "Pisces": "imaginative, creative, kind, supportive, people-smart, emotional intelligent, intuitive (even psychic), and able to see beyond the façade to the truth of things."
    }
        if (self.month == 3 and self.day >= 21) or (self.month == 4 and self.day <= 19):
            return "Aries", zodiac_signs['Aries']
        elif (self.month == 4 and self.day >= 20) or (self.month == 5 and self.day <= 20):
            return "Taurus", zodiac_signs['Taurus']
        elif (self.month == 5 and self.day >= 21) or (self.month == 6 and self.day <= 20):
            return "Gemini", zodiac_signs['Gemini']
        elif (self.month == 6 and self.day >= 21) or (self.month == 7 and self.day <= 22):
            return "Cancer", zodiac_signs['Cancer']
        elif (self.month == 7 and self.day >= 23) or (self.month == 8 and self.day <= 22):
            return "Leo", zodiac_signs['Leo']
        elif (self.month == 8 and self.day >= 23) or (self.month == 9 and self.day <= 22):
            return "Virgo", zodiac_signs['Virgo']
        elif (self.month == 9 and self.day >= 23) or (self.month == 10 and self.day <= 22):
            return "Libra", zodiac_signs['Libra']
        elif (self.month == 10 and self.day >= 23) or (self.month == 11 and self.day <= 21):
            return "Scorpio", zodiac_signs['Scorpio']
        elif (self.month == 11 and self.day >= 22) or (self.month == 12 and self.day <= 21):
            return "Sagittarius", zodiac_signs['Sagittarius']
        elif (self.month == 12 and self.day >= 22) or (self.month == 1 and self.day <= 19):
            return "Capricorn", zodiac_signs['Capricorn']
        elif (self.month == 1 and self.day >= 20) or (self.month == 2 and self.day <= 18):
            return "Aquarius", zodiac_signs['Aquarius']
        elif (self.month == 2 and self.day >= 19) or (self.month == 3 and self.day <= 20):
            return "Pisces", zodiac_signs['Pisces']
        else:
            return "Invalid input", ""
        
    def __str__(self):
        zodiac_sign, characteristics = self.get_zodiac_signs()
        return f"Zodiac sign: {zodiac_sign}\nCharacteristics: {characteristics}"

    def display_info(self):
        print({self.month}, {self.day})

class Birthday(Zodiac):
    def __init__(self,month, day, year, name):
        super().__init__(month, day)
        self.year = year
        self.name = name

    def height(self):
        pass
    
    def display_info(self):
        super().display_info()
        
        print({key: value for key, value in enumerate([self.name, self.day, self.month, self.year])}) 

  


def main():
        name = input("Enter your name: \n ")
        month = int(input("Enter your birth month (as a number): "))
        day = int(input("Enter your birth day (as a number): "))
        year = int(input("enter your year of birth"))
        calculate_age = lambda year: datetime.now().year - year
        
        age = calculate_age(year)

        Birthday_obj = Birthday(month,day,year,name)
        Zodiac_sign = Zodiac(month,day)
        sign, characteristics = Zodiac_sign.get_zodiac_signs()
        while sign != "Invalid input":
            print(name)
            time.sleep(1)
            print("Your zodiac sign is:", sign)
            time.sleep(1)
            print("Characteristics of", sign, ":", characteristics)
            time.sleep(1)
            Birthday_obj.display_info()
            time.sleep(1)
            print(f"You are {age} years old.")
            time.sleep(1)
            try:
                with open(f"{name}.txt",'r')as file:
                    print("wait you have been here before, i remember you, here is your info:")
                    print(file.read())
                    print("please come back again")
            except:
                with open (f"{name}.txt", 'w') as file:
                    file.write(f"name: {name} \n age: {age} \n date of birth: {year} \n sign: {sign} \n characteristics: {characteristics}  ")
                    print(f"name is: {name}\n \n date of birth: {year}\n your sign is : {sign} \n your characteristics are : {characteristics}")

                    print("you can always accesss your information here")
            
            print("thanks for checking us out, tell a friend to tell a friend")
            break
        else:
            print("Invalid input. Please enter a valid month and day.")

def data_science():
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

#this function helps us determine how old our custoers will be the next year
    def add_one(x):
        return x+1
    values_for_ages = data['Ages']
    #we use the map function to add a year to each of our custoerr's ages
    added_val =map(add_one,values_for_ages)
    added_val_list = list(added_val)
    print(f"next year these are the ages of our users: {added_val_list}")

    df = pd.DataFrame(data)
    ages_list = data['Ages']
    print(f" ages list is: {ages_list}")

    df = pd.DataFrame(data)
    df[dob] = pd.to_datetime(df['dob']) 
    ages_list = data['Ages']
    
    #this turns the key Ages in the dictionary into a list
    ages_list = data['Ages']
    print(ages_list)
    #this turns the ages list into an array
    age_array = np.array(ages_list)
    #we use pandas to find the average age of our users
    mean_age = np.mean(age_array)
    print(mean_age)

    
    name_list = data['Names']
    print(name_list)
    #bar graph
    plt.bar(name_list,ages_list,color='blue')
    plt.xlabel("names")
    plt.ylabel('age')
    plt.title('A bar graph')
    plt.grid(axis='y')
    plt.show()

if __name__ == "__main__":
    main()
    data_science()
    