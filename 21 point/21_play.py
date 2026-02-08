import random as r

def ochko():
    return r.randint(1, 11)


def game():
    print("------------------")
    print("|'игра в 21 очко'|")
    print("------------------")
    print("| диллер бросает,|")
    print("| если него < 17 |")
    print("------------------")
    
    player_ochko = 0
    dealer_ochko = 0
    

    while True:
        if player_ochko:
            print()
            print(f"Ваш счёт: {player_ochko}")
        print()
        print("------------------")
        print("|'+' кинуть кости|")
        print("|'-' остановиться|")
        print("------------------")
        print()
        
        s = input("примите решение для игры: ")
        
        
        while s not in ["+", "-"]:
            s = input("введите корректное значение ('+' или '-'): ")

        if s == "+":
            player_ochko += ochko()
        
            if player_ochko == 21:
                print(f"Ваш счёт: {player_ochko}")
                print()
                print("*********************")
                print("* вы выйграли игру! *")
                print("*  диллер проиграл  *")
                print("*********************")
                print()
                break
        
            elif player_ochko > 21:
                print(f"Ваш счёт: {player_ochko}")
                print()
                print("#####################")
                print("#  диллер выйграл!  #")
                print("#   вы проиграли    #")
                print("#####################")
                print()
                break
        else:
        
                while dealer_ochko < 17:
                    dealer_ochko += ochko()

                
                
                if dealer_ochko > 21 or dealer_ochko < player_ochko:
                    print()
                    print("*********************")
                    print("* вы выйграли игру! *")
                    print("* диллер 'перебрал' *")
                    print("*********************")
                    print()
                    print(f"--- ИТОГ ---")
                    print(f"Ваши очки: {player_ochko}")
                    print(f"Очки дилера: {dealer_ochko}\n")
                    break
                elif dealer_ochko == player_ochko:
                    print()
                    print("*********************")
                    print("* вы сыграли вничью *")
                    print("*    переиграйте    *")
                    print("*********************")
                    print()
                    break
                elif dealer_ochko > player_ochko:
                    print()
                    print("#####################")
                    print("#  диллер выйграл!  #")
                    print("#   вы проиграли    #")
                    print("#####################")
                    print()
                    print(f"--- ИТОГ ---")
                    print(f"Ваши очки: {player_ochko}")
                    print(f"Очки дилера: {dealer_ochko}\n")
                    break


while True:                   
    game()
    if input("Нажмите enter чтобы играть заново, либо напишите как вам игра и сеанс завершится: "):
        break
