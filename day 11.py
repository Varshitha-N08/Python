# # # # password=input("Enter your password:")
# # # # alpha=""
# # # # digit=""
# # # # special=""
# # # # for ch in password:
# # # #     if ch.isalpha():
# # # #         alpha+=ch
# # # #     elif ch.isdigit():
# # # #         digit+=ch
# # # #     else:
# # # #         special+=ch
# # # # if len(digit)==2 and len(special)==1 and len(alpha)>=3:
# # # #     print("Password is valid")
# # # # else:
# # # #     print("Password is not valid")

# # #prg2
# # # s = input("Enter a sentence: ")
# # # count = 0

# # # for ch in s.lower():
# # #     if ch in "aeiou":
# # #         count = count + 1

# # # print("Number of vowels:", count)  


# # #prg 3
# # name = "Arjun"
# # marks = 95

# # print(f"{name} scored {marks} marks")


# #prg 4
# name = "Arjun"
# marks = 95

# print("{} scored {} marks".format(name, marks))  

#prg 5
password = input("Enter password: ")

if len(password) >= 8 and any(ch.isupper() for ch in password):
    print("Valid password")
else:
    print("Invalid password")

