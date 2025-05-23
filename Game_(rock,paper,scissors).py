# GAME (rock, paper, scissors)

print('\n')
Players = input("Hello,\nHow many players want to play the Rock, Paper, Scissors game? = ")
if (int(Players) <= 0):
    print("Invalid input!")

elif (int(Players) == 1):
    print("This game can't be played solo!")

elif (int(Players) == 2):
    print('Ok! This game can be played with two players.')
    Ready = input("Are you ready to play the Rock, Paper, Scissors game? (Yes/No) = ")
    if Ready.lower() == 'yes':
        p1 = input("Enter player 1 name: ")
        p2 = input("Enter player 2 name: ")
        p1 = ' '.join(p1.split())
        if p1.replace(" ", "").isalpha():
            p2 = ' '.join(p2.split())
            if p2.replace(" ", "").isalpha():
                print('_____(GAME START!)_____')
                p1_str = input(f'Enter {p1}, your choice (rock, paper, scissors)? = ')
                p1_str = ' '.join(p1_str.split())
                if p1_str.replace(" ", "").isalpha():
                    p2_str = input(f'Enter {p2}, your choice (rock, paper, scissors)? = ')
                    p2_str = ' '.join(p2_str.split())
                    if p2_str.replace(" ", "").isalpha():
                        p_set = {"rock": 0, "paper": 1, "scissors": 2}
                        rev_set = {0: "rock", 1: "paper", 2: "scissors"}

                        you1 = p_set.get(p1_str.lower())
                        you2 = p_set.get(p2_str.lower())

                        if you1 is None or you2 is None:
                            print("Invalid choices! Please choose rock, paper, or scissors.")
                        else:
                            print('')
                            print(f"{p1}, your choice is: {rev_set[you1]}")
                            print(f"{p2}, your choice is: {rev_set[you2]}")
                            print('')

                            if you1 == you2:
                                print("It's a draw!")
                            elif (you1 == 0 and you2 == 1):
                                print(f"{p2} wins!")
                            elif (you1 == 0 and you2 == 2):
                                print(f"{p1} wins!")
                            elif (you1 == 1 and you2 == 0):
                                print(f"{p1} wins!")
                            elif (you1 == 1 and you2 == 2):
                                print(f"{p2} wins!")
                            elif (you1 == 2 and you2 == 0):
                                print(f"{p2} wins!")
                            elif (you1 == 2 and you2 == 1):
                                print(f"{p1} wins!")
                    else:
                        print(f"{p2_str} is not a valid input! (rock, paper, scissors)?")
                else:
                    print(f"{p1_str} is not a valid input! (rock, paper, scissors)?")
            else:
                print(f"Please enter a valid name for {p2}!")
        else:
            print(f"Please enter a valid name for {p1}!")
    else:
        print("Ok! Game closing...")

elif (int(Players) == 3):
    print("Ok! This game can be played with 3 players.")
    Ready2 = input("Are you ready to play the Rock, Paper, Scissors game? (Yes/No) = ")
    if Ready2.lower() == 'yes':
        p1 = input("Enter player 1 name: ")
        p2 = input("Enter player 2 name: ")
        p3 = input("Enter player 3 name: ")
        p1 = ' '.join(p1.split())
        if p1.replace(" ", "").isalpha():
            p2 = ' '.join(p2.split())
            if p2.replace(" ", "").isalpha():
                p3 = ' '.join(p3.split())
                if p3.replace(" ", "").isalpha():
                    print('_____(GAME START!)_____')
                    p1_str = input(f'Enter {p1}, your choice (rock, paper, scissors)? = ')
                    p1_str = ' '.join(p1_str.split())
                    if p1_str.replace(" ", "").isalpha():
                        p2_str = input(f'Enter {p2}, your choice (rock, paper, scissors)? = ')
                        p2_str = ' '.join(p2_str.split())
                        if p2_str.replace(" ", "").isalpha():
                            p3_str = input(f'Enter {p3}, your choice (rock, paper, scissors)? = ')
                            p3_str = ' '.join(p3_str.split())
                            if p3_str.replace(" ", "").isalpha():
                                rps = {"rock": 0, "paper": 1, "scissors": 2}
                                rev = {0: "rock", 1: "paper", 2: "scissors"}

                                you1 = rps.get(p1_str.lower())
                                you2 = rps.get(p2_str.lower())
                                you3 = rps.get(p3_str.lower())

                                if None in (you1, you2, you3):
                                    print("Invalid choices! Please choose rock, paper, or scissors.")
                                else:
                                    print('')
                                    print(f"{p1}, your choice is: {rev[you1]}")
                                    print(f"{p2}, your choice is: {rev[you2]}")
                                    print(f"{p3}, your choice is: {rev[you3]}")
                                    print('')

                                    if (you1 == you2 == you3):
                                        print("It's a draw!")
                # 0
                                    elif (you1 == 0 and you2 == 1 and you3 == 2):
                                        print("No one wins!")
                                
                                    elif (you1 == 0 and you2 == 2 and you3 == 1):
                                        print("No one wins!")
                                    
                                    elif (you1 == 0 and you2 == 1 and you3 == 1):
                                        print(f"{p2} and {p3} win!")
                                
                                    elif (you1 == 0 and you2 == 2 and you3 == 2):
                                        print(f"{p1} wins!")

                                    elif (you1 == 0 and you2 == 1 and you3 == 0):
                                        print(f"{p2} wins!")

                                    elif (you1 == 0 and you2 == 0 and you3 == 1):
                                        print(f"{p3} wins!")

                                    elif (you1 == 0 and you2 == 0 and you3 == 2):
                                        print(f"{p1} and {p2} win!")        
                # 1
                                    elif (you1 == 1 and you2 == 2 and you3 == 0):
                                        print("No one wins!")
                                
                                    elif (you1 == 1 and you2 == 0 and you3 == 2):
                                        print("No one wins!")
                                    
                                    elif (you1 == 1 and you2 == 0 and you3 == 0):
                                        print(f"{p1} wins!")
                                
                                    elif (you1 == 1 and you2 == 2 and you3 == 2):
                                        print(f"{p2} and {p3} win!")

                                    elif (you1 == 1 and you2 == 0 and you3 == 1):
                                        print(f"{p1} and {p3} win!")

                                    elif (you1 == 1 and you2 == 1 and you3 == 0):
                                        print(f"{p1} and {p2} win!")

                                    elif (you1 == 1 and you2 == 1 and you3 == 2):
                                        print(f"{p3} wins!")            
                # 2
                                    elif (you1 == 2 and you2 == 1 and you3 == 0):
                                        print("No one wins!")
                                
                                    elif (you1 == 2 and you2 == 0 and you3 == 1):
                                        print("No one wins!")
                                    
                                    elif (you1 == 2 and you2 == 0 and you3 == 0):
                                        print(f"{p2} and {p3} win!")
                                
                                    elif (you1 == 2 and you2 == 1 and you3 == 1):
                                        print(f"{p1} wins!")

                                    elif (you1 == 2 and you2 == 0 and you3 == 2):
                                        print(f"{p2} wins!")

                                    elif (you1 == 2 and you2 == 2 and you3 == 0):
                                        print(f"{p3} wins!")

                                    elif (you1 == 2 and you2 == 2 and you3 == 1):
                                        print(f"{p1} and {p2} win!")
                            else:
                                print(f"{p3_str} is not a valid input! (rock, paper, scissors)")
                        else:
                            print(f"{p2_str} is not a valid input! (rock, paper, scissors)")
                    else:
                        print(f"{p1_str} is not a valid input! (rock, paper, scissors)")
                else:
                    print(f"Please enter a valid name for {p3}!")
            else:
                print(f"Please enter a valid name for {p2}!")
        else:
            print(f"Please enter a valid name for {p1}!")
    else:
        print("Ok! Game closing...")

elif (int(Players) > 3):
    print(f"This game can't be played with {Players} players!")
