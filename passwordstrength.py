

print("Loading password list...")
with open("/usr/share/wordlists/rockyou.txt", "r", encoding="latin-1") as f:
    common_passwords = set(line.strip() for line in f)
with open("passwords_lt.txt", "r", encoding="latin-1") as f:
    lt_passwords = set(line.strip() for line in f)


common_passwords = common_passwords | lt_passwords


while True:
    password = input("Enter your Password:")
    length = len(password)



    if password.lower() in common_passwords:
        print("This password is too common! Choose another.")
        continue

    if length < 8:
        print("Password is too short. Try again.")
        continue


    score = 0
    has_number = False
    has_upper = False
    has_lower = False
    has_special = False


    for char in password:
        if char.isdigit():
            has_number = True

        if char.isupper():
            has_upper = True

        if char.islower():
            has_lower = True

        if not char.isalnum():
            has_special = True


    if length>= 8:
        score += 1

    if has_number:
        score += 1

    if has_upper:
        score += 1

    if has_lower:
        score += 1

    if has_special:
        score += 1




    print("Score:", score)


    if score <= 1:
        print("Password strength: Weak")
    elif score == 2 or score == 3:
        print("Password strength: Medium")
    else:
        print("Password strength: Strong")

    break
