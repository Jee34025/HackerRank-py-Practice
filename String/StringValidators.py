if __name__ == '__main__':
    s = input()
    flag_alnum = False
    flag_alpha = False
    flag_digit = False
    flag_lower = False
    flag_upper = False

    for i in s :
        if i.isalnum():
            flag_alnum = True
        if i.isalpha():
            flag_alpha = True
        if i.isdigit():
            flag_digit = True
        if i.islower():
            flag_lower = True
        if i.isupper():
            flag_upper = True
    
    print(flag_alnum)
    print(flag_alpha)
    print(flag_digit)
    print(flag_lower)
    print(flag_upper)