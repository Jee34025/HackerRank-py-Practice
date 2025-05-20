def mutate_string(string, position, character):
    add_chars = list(string)
    add_chars[position] = character
    return "".join(add_chars)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)