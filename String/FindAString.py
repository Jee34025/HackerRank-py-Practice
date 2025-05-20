def count_substring(string,substring):
    n = 0
    for i in range(len(string) - len(substring) +1):
        if string[i : i + len(substring)] == substring :
            n += 1
    return n

if __name__ == '__main__':
    string = input().strip()
    substring = input().strip()
    print(count_substring(string,substring))
