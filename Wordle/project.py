import random

from colorama import init, Fore, Back, Style
init(autoreset=True)


with open('text.txt', 'r', encoding='utf-8') as file:
    infa = [line.strip("\n").lower() for line in file if len(line.strip("\n")) == 5]

slovo = random.choice(infa)
    
def proverka(s, slovo):
    for i in range(5):
        if s[i] == slovo[i]:
            print(Back.YELLOW + "\033[30m" + s[i], end="")
        elif s[i] in slovo:
            print(Back.WHITE + "\033[30m" + s[i], end="")
        else:
            print(Back.WHITE + "\033[48;5;244m" + s[i], end="")
    print()




s = input("Введите слово: ")
while len(s) == 5:
    proverka(s, slovo)
    s = input("Введите слово: ")
else:
    print('Введите слово из 5 букв в следующей игре!')
