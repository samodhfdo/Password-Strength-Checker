import re


def check_password(password):
    score = 0
    if (len(password)) >= 8:
        score += 1
    if re.search("[A-Z]", password):
        score += 1
    if re.search("[a-z]", password):
        score += 1
    if re.search("[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*()_+~?><*/\|]", password):
        score += 1
    return score


password = input("Enter your password: ")
score = check_password(password)
if score <= 2:
    print("Your Password is Weak!")
elif score == 3 or score == 4:
    print("Your Password is Medium!")
elif score == 5:
    print("Your Password is Strong!")
