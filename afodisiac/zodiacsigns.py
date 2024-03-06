import time
from datetime import datetime   
class Zodiac:

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
                    print("please coe back again")
            except:
                with open (f"{name}.txt", 'w') as file:
                    file.write(f"name: {name}\n, sign: {sign}, characteristics: {characteristics}  ")
                    print(f"name is: {name}\n your sign is : {sign}\n your characteristics are : {characteristics}")
                    print("you can always accesss your information here")
            
            print("thanks for checking us out, tell a friend to tell a friend")
            break
        else:
            print("Invalid input. Please enter a valid month and day.")


if __name__ == "__main__":
    main()
    