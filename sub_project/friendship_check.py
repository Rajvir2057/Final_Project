 
#I want to form a cute word game using len(), like i mean it will do this see yea,
name1= input("Enter your name here please: ")
name_len1 = len(name1)
print(f"The name length of your name is: {name_len1}\n")

name2= input("Enter your friend's name here please: ")
name_len2 = len(name2)
print(f"the name length of your name is: {name_len2}\n")

print("-----------------------------------------------")

def add_div(len1,len2):
    return (len1+len2)//2
answer= add_div(name_len1, name_len2)
print(f"The total of the test is: {answer} \n")
print("-----------------------------------------------")

if answer <= 5:
    print("you guys are cute friends")

elif answer >= 6:
    print("you guys are besties!")

elif answer >= 10:
    print("damn, this friendship will last long.")

else:
    print("I have nothing to say!")


