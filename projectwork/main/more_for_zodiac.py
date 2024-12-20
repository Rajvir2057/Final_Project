
def write_file():
        file =open('lucky1.txt', 'w')
        file.write("Sagittarius => 3\n")
        file.close()

        file= open("lucky1.txt", "a")
        file.write("Capricorn => 4\n")
        file.write("Aquarius  => 11\n")
        file.write("Pisces  => 7\n")
        file.write("Aries  => 9\n")
        file.write("Taurus  => 5 and 6\n")
        file.write("Gemini => 5\n")
        file.write("Cancer  => 2\n")
        file.write("Leo => 1\n")
        file.write("Virgo  => 3\n")
        file.write("Libra  => 7\n")
        file.write("Scorpio => 8\n")
write_file()

class Compactibility:
    def __init__(self, zodiac1, zodiac2):
        self.zodiac1 = zodiac1.lower()
        self.zodiac2 = zodiac2.lower()

    def zod_compact(self):
        if self.zodiac1 == 'sagittarius':
            if self.zodiac2 == 'aries':
                print("High chances of being together.")
            elif self.zodiac2 == 'leo':
                print("Medium chances of being together.")
            elif self.zodiac2 == 'libra':
                print("Low chances of being together.")
            else:
                print("Sorry you can not be together.")

        elif self.zodiac1 == 'capricorn':
            if self.zodiac2 == 'taurus':
                print("High chances of being together.")
            elif self.zodiac2 == 'virgo':
                print("Medium chances of being together.")
            elif self.zodiac2 == 'scorpio':
                print("Low chances of being together.")
            else:
                print("Sorry you can not be together.")

        elif self.zodiac1 == 'aquarius':
            if self.zodiac2 == 'gemini':
                print("High chances of being together.")
            elif self.zodiac2 == 'libra':
                print("Medium chances of being together.")
            elif self.zodiac2 == 'sagittarius':
                print("Low chances of being together.")
            else:
                print("Sorry you can not be together.")

        elif self.zodiac1 == 'pisces':
            if self.zodiac2 == 'cancer':
                print("High chances of being together.")
            elif self.zodiac2 == 'scorpio':
                print("Medium chances of being together.")
            elif self.zodiac2 == 'taurus':
                print("Low chances of being together.")
            else:
                print("Sorry you can not be together.")

        elif self.zodiac1 == 'aries':
            if self.zodiac2 == 'leo':
                print("High chances of being together.")
            elif self.zodiac2 == 'sagittarius':
                print("Medium chances of being together.")
            elif self.zodiac2 == 'gemini':
                print("Low chances of being together.")
            else:
                print("Sorry you can not be together.")

        elif self.zodiac1 == 'taurus':
            if self.zodiac2 == 'virgo':
                print("High chances of being together.")
            elif self.zodiac2 == 'capricorn':
                print("Medium chances of being together.")
            elif self.zodiac2 == 'cancer':
                print("Low chances of being together.")
            else:
                print("Sorry you can not be together.")

        elif self.zodiac1 == 'gemini':
            if self.zodiac2 == 'libra':
                print("High chances of being together.")
            elif self.zodiac2 == 'aquarius':
                print("Medium chances of being together.")
            elif self.zodiac2 == 'aries':
                print("Low chances of being together.")
            else:
                print("Sorry you can not be together.")

        elif self.zodiac1 == 'cancer':
            if self.zodiac2 == 'scorpio':
                print("High chances of being together.")
            elif self.zodiac2 == 'pisces':
                print("Medium chances of being together.")
            elif self.zodiac2 == 'taurus':
                print("Low chances of being together.")
            else:
                print("Sorry you can not be together.")

        elif self.zodiac1 == 'leo':
            if self.zodiac2 == 'sagittarius':
                print("High chances of being together.")
            elif self.zodiac2 == 'aries':
                print("Medium chances of being together.")
            elif self.zodiac2 == 'gemini':
                print("Low chances of being together.")
            else:
                print("Sorry you can not be together.")

        elif self.zodiac1 == 'virgo':
            if self.zodiac2 == 'capricorn':
                print("High chances of being together.")
            elif self.zodiac2 == 'taurus':
                print("Medium chances of being together.")
            elif self.zodiac2 == 'cancer':
                print("Low chances of being together.")
            else:
                print("Sorry you can not be together.")

        elif self.zodiac1 == 'libra':
            if self.zodiac2 == 'aquarius':
                print("High chances of being together.")
            elif self.zodiac2 == 'gemini':
                print("Medium chances of being together.")
            elif self.zodiac2 == 'leo':
                print("Low chances of being together.")
            else:
                print("Sorry you can not be together.")

        elif self.zodiac1 == 'scorpio':
            if self.zodiac2 == 'pisces':
                print("High chances of being together.")
            elif self.zodiac2 == 'cancer':
                print("Medium chances of being together.")
            elif self.zodiac2 == 'virgo':
                print("Low chances of being together.")
            else:
                print("Sorry you can not be together.")
                
        else:
            print("Invalid zodiac signs entered.")


             