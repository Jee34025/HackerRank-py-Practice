def swap_case(s):
    update_s = ""

    for i in s :
        if i.isupper():
            update_s += i.lower()
        elif i.islower():
            update_s += i.upper()
        else:
            update_s += i
    return update_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
