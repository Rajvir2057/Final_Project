import time 
import csv 
import os
#This is a simple input.
input("Enter Your Name :) :  ") 
print("....................................................")
print("WELCOME TO RAJ.ZODIAC SIGNS.. HOPE YOU ENJOY.")
print("....................................................")
#Here i used a class that uses inheritence...
class Zodiac:
    def __init__(self,day,month):
        self.day= day
        self.month= month


class Raj_zodiac(Zodiac):

    running = True #used a boolean format..

    while running:   
        day= int(input("Please Enter Your Birthday day only: "))

        print("Choose Your Month.")
        print("1.January")
        print("2.February")
        print("3.March")
        print("4.April")
        print("5.May")
        print("6.June")
        print("7.July")
        print("8.August")
        print("9.September")
        print("10.October")
        print("11.November")
        print("12.December")

        month= input("Please Enter Your Choice: ")

        if month == '12':
            astro_sign = 'Sagittarius' if (day < 22) else 'Capricorn' 
        if month == '1':
            astro_sign = 'Capricorn' if (day < 20) else 'Aquarias'
        if month == '2':
            astro_sign = 'Aquarias' if (day < 19) else 'Pisces'
        if month == '3':
            astro_sign = 'Pisces' if (day < 21) else 'Aries'
        if month == '4':
            astro_sign = 'Aries' if (day < 20) else 'Taurus'
        if month == '5':
            astro_sign = 'Taurus' if (day < 21) else 'Gemini'
        if month == '6':
            astro_sign = 'Gemini' if (day < 21) else 'Cancer'
        if month == '7':
            astro_sign = 'Cancer' if (day < 23) else 'Leo'
        if month == '8':
            astro_sign = 'Leo'   if (day < 23) else 'Virgo'
        if month == '9':
            astro_sign = 'Virgo' if (day < 23) else 'Libra'
        if month == '10':
            astro_sign = 'Libra' if (day < 23) else 'Scorpio'
        if month == '11':
            astro_sign = 'Scorpio' if (day< 22) else  'Sagittarius'

        print("______________________________________________________")
        print (f"Your Zodiac Sign Is:  {astro_sign}")
        print("______________________________________________________")
        if astro_sign== "Sagittarius":
            file= open("try2.txt","r")
            line= file.readlines()
            print(line[0])
            print(line[1])
            print(line[2])
            print(line[3])
            print(line[4])
            print(line[5])

        elif astro_sign== "Capricorn":
            file= open("try2.txt","r")
            line= file.readlines()
            print(line[7])
            print(line[8])
            print(line[9])
            print(line[10])
            print(line[11])
            print(line[12])

        elif astro_sign== "Aquarias":
            file= open("try2.txt","r")
            line= file.readlines()
            print(line[14])
            print(line[15])
            print(line[16])
            print(line[17])
            print(line[18])
            print(line[19])
            
        elif astro_sign== "Pisces":
            file= open("try2.txt","r")
            line= file.readlines()
            print(line[21])
            print(line[22])
            print(line[23])
            print(line[24])
            print(line[25])
            print(line[26])

        elif astro_sign== "Aries":
            file= open("try2.txt","r")
            line= file.readlines()
            print(line[28])
            print(line[29])
            print(line[30])
            print(line[31])
            print(line[32])
            print(line[33])

        elif astro_sign== "Taurus":
            file= open("try2.txt","r")
            line= file.readlines()
            print(line[35])
            print(line[36])
            print(line[37])
            print(line[38])
            print(line[39])
            print(line[40])

        elif astro_sign== "Gemini":
            file= open("try2.txt","r")
            line= file.readlines()
            print(line[42])
            print(line[43])
            print(line[44])
            print(line[45])
            print(line[46])
            print(line[47])

        elif astro_sign== "Cancer":
            file= open("try2.txt","r")
            line= file.readlines()
            print(line[49])
            print(line[50])
            print(line[51])
            print(line[52])
            print(line[53])
            print(line[54])

        elif astro_sign== "Leo":
            file= open("try2.txt","r")
            line= file.readlines()
            print(line[56])
            print(line[57])
            print(line[58])
            print(line[59])
            print(line[60])
            print(line[61])

        elif astro_sign== "Virgo":
            file= open("try2.txt","r")
            line= file.readlines()
            print(line[63])
            print(line[64])
            print(line[65])
            print(line[66])
            print(line[67])
            print(line[68])
            print(line[69])

        elif astro_sign== "Libra":
            file= open("try2.txt","r")
            line= file.readlines()
            print(line[70])
            print(line[71])
            print(line[72])
            print(line[73])
            print(line[74])
            print(line[75])

        elif astro_sign== "Scorpio":
            file= open("try2.txt","r")
            line= file.readlines()
            print(line[77])
            print(line[78])
            print(line[79])
            print(line[80])
            print(line[81])
            print(line[82])

        else:
            print("Thats unfortunate..")
    
        if input("Do You want to check again? (yes/no): ")== "no":
            running= False
            
print("_______________________________________________________________________")

print("Hello, Thank your for checking your sign.")
time.sleep(2)
lucky_fortune=("This will help you learn your lucky number for good fortune.")
upper_case = lucky_fortune.upper()
print(upper_case)

print('.......................................................................')
time.sleep(1)
print("A little fact!.")
data_for_delay=["Do","you","know","your","lucky","number","can","help","in","bringing","good fortune."]
for index, word in enumerate(data_for_delay):
    print(word, end= " ", flush= True)
    time.sleep(1)

print("Time to know your lucky number \n")

zod_sign = input("Enter your zodiac sign.: ")

try:
    with open('lucky1.txt', 'r') as file:
        lines = file.readlines()

    zod_sign = zod_sign.strip().lower()

    print("Input Zodiac Sign:", zod_sign)

    if zod_sign == 'sagittarius':
        print(lines[0])
    elif zod_sign == 'capricorn':
        print(lines[1])
    elif zod_sign == 'aquarius':
        print(lines[2])
    elif zod_sign == 'pisces':
        print(lines[3])
    elif zod_sign == 'aries':
        print(lines[4])
    elif zod_sign == 'taurus':
        print(lines[5])
    elif zod_sign == 'gemini':
        print(lines[6])
    elif zod_sign == 'cancer':
        print(lines[7])
    elif zod_sign == 'leo':
        print(lines[8])
    elif zod_sign == 'virgo':
        print(lines[9])
    elif zod_sign == 'libra':
        print(lines[10])
    elif zod_sign == 'scorpio':
        print(lines[11])
    else:
        print("Invalid zodiac sign!")

except FileNotFoundError:
    print("This file does not exist.")
("\n")
# this is now reading a csv file with lines...
print("Time to know your lucky colour.")
("\n")
Entry = input("Please enter your zodiac sign again!: ").lower()

if os.path.exists('zodiac_color_record.csv'):
    with open('zodiac_color_record.csv', 'r') as file:
        reader = csv.reader(file)
        for zodiac_sign, lucky_color in reader:
            if zodiac_sign.lower() == Entry:
                print(f"The lucky color for {zodiac_sign} is: {lucky_color}")
                break
        else:
            print("Hmm. This was not expected.")
else:
    print("The CSV file does not exist.")


from more_for_zodiac import Compactibility

class Zodiac_compatibility(Compactibility):
    def __init__(self):
        self.zodiac1 = input("Enter your zodiac sign please.: ")
        self.zodiac2 = input("Enter your partner's zodiac sign please.: ")
    
    def calculate_compatibility(self):
        compact= Compactibility(self.zodiac1, self.zodiac2)
        compact.zod_compact()
zodiac_comp = Zodiac_compatibility()
zodiac_comp.calculate_compatibility()
