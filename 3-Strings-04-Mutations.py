def mutate_string(string, position, character):
    line = list(string)
    line[position] = character
    newstring = ''.join(line)
    return newstring
    
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
