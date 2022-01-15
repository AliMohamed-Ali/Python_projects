#1-import module
# 2-store all character ivarible in lists(uper / lower case - digits -punctuations)
# 3-take numper of character from user
# 4-make sure the number of character is 6 or more
# 5-shuffle all list ==>import module random
# 6-calculate 30% and 20% the number of character
# 7-create password 60%letters and 40% digits and punctuatioins
import string
import random
s1=list(string.ascii_lowercase)
s2=list(string.ascii_uppercase)
s3=list(string.digits)
s4=list(string.punctuation)
character_number = input("Enyer the number of character password?: ")
while True:
    try:
        character_number = int(character_number)
        if int(character_number) < 6 :
            print("please enter at leaste 6 character")
            character_number = input("Enyer the number of character password again ?: ")
        else:
            print("Thank you!")
            break
    except:
        character_number = input("please Enyer the number of character password digits only?: ")

# shuffle all list
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

# the password consist of two parts part 1 character and part2 digits and punctuations

password =[]

part1 = round(character_number *(30/100))
part2 = round(character_number *(20/100))
for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])

for i in range(part2):
    password.append(s3[i])
    password.append(s4[i])

# print(password)
# shuffle for new password
random.shuffle(password)
password = "".join(password[:])
print(password)
