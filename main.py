# Welcome message
print("Welcome to the Love Calculator")

name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

combined_names = name1 + name2

true_count = 0
love_count = 0

true_count += combined_names.count("t")
true_count += combined_names.count("r")
true_count += combined_names.count("u")
true_count += combined_names.count("e")
love_count += combined_names.count("l")
love_count += combined_names.count("o")
love_count += combined_names.count("v")
love_count += combined_names.count("e")

score_string = str(true_count) + str(love_count)
score_final = int(score_string)

if score_final < 10 or score_final > 90:
    message = ", you get together like coke and mentos"
elif 40 <= score_final <= 50:
    message = ", you are alright together"
else:
    message = ""

print(f"Your score is {score_final}{message}.")