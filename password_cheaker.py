def check_password(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(not c.isalnum() for c in password):
        score += 1
    print("\nPassword Strength:")
    if score <= 2:
        print("Weak")
    elif score == 3 or score == 4:
        print("Medium")
    else:
        print("Strong")
password = input("Enter a password: ")
check_password(password)