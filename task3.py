def check_password(password):
    n = len(password)
    lower = upper = number = char = False
    if n < 6 or n > 16 :
        return False
    else:
        for i in password:
            if i >= 'a' and i <= 'z':
                lower = True
            if i >= 'A' and i <= 'Z':
                upper = True
            if i >= '0' and i <= '9':
                number = True
            if i == '$' or i == '#' or i == '@':
                char = True
        if lower == True and upper == True and number == True and char == True:
            return True
def main():
    password = input()
    if check_password(password):
        print("Password is valid")
    else:
        print("password is invalid")
if __name__ == "__main__":
    main()