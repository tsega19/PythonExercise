# String problem for hacker rank 
# -----Exercies 1--------
# Python UperCase to LowerCase
def swap_case(sentence):
    updated_s = ""
    for c in sentence:
        if c.isupper():
            updated_s += c.lower()
        elif c.islower():
            updated_s += c.upper()
        else:
            updated_s += c
    return updated_s
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
# --------Exercise 2----------
# Split to Join and Join to split
def split_and_join(line):
    joinSplit ="".join(line)
    return joinSplit
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
#------Exercise 3----------
# Wrire your name

def print_full_name(first, last):
  print("Hello {} {}! You just delved into python." .format(first, last))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
#---------Exercise 4-----------
# Mutation
def mutate_string(string, position, character):
    chars = list(string)
    chars[position] = character
    return "".join(chars)
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
#-------- Exercies 5------------
def count_substring(string, sub_string):
    count_sub_string = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i + len(sub_string)] == sub_string:
            count_sub_string += 1
    return count_sub_string
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)