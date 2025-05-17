def print_full_name(frist,last):
    return (f"Hello {frist} {last}! You just delved into python.")

if __name__ == '__main__' :
    frist = input()
    last = input()
    result = print_full_name(frist,last)

print(result)