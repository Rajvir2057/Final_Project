
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
zodiac1 = input("Enter your zodiac sign: ")

print("choose one of the following options.")
print("1. Sagittarius")
print("2. Capricorn")
print("3. Aquarius")
print("4. Pisces")
print("5. Aries")
print("6. Taurus")
print("7. Gemini")
print("8. Cancer")
print("9. Leo")
print("10. Virgo")
print("11. Libra")
print("12.Scorpio")
zodiac2 = input("select any option above.")

if zodiac1 == 