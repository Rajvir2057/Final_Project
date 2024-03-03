import time 

print("Hello, Thank your for checking your sign.")
time.sleep(2)
lucky_fortune=("This will help you learn your lucky number for good fortune.")
upper_case = lucky_fortune.upper()
print(upper_case)

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
print('...........................................')
time.sleep(1)
print("A little fact!.")
data_for_delay=["Do","you","know","your","lucky","number","can","help","in","bringing","good fortune."]
for index, word in enumerate(data_for_delay):
    print(word, end= " ", flush= True)
    time.sleep(2)

