print('\n')

while True:
    Players = input("Hello,\nHow many players want to play the Rock, Paper, Scissors game? = ")
    if not Players.isdigit() or int(Players) <= 0:
        print("Invalid input!")
        continue

    Players = int(Players)

    if Players == 1:
        print("This game can't be played solo!")

    elif Players == 2:
        print('Ok! This game can be played with two players.')
        Ready = input("Are you ready to play the Rock, Paper, Scissors game? (Yes/No) = ")
        if Ready.lower() != 'yes':
            print("Ok! Game closing...")
            break

        p1 = input("Enter player 1 name: ").strip()
        p2 = input("Enter player 2 name: ").strip()

        if not (p1.replace(" ", "").isalpha() and p2.replace(" ", "").isalpha()):
            print("Please enter valid names for both players!")
            continue

        print('_____(GAME START!)_____')
        p1_str = input(f'Enter {p1}, your choice (rock, paper, scissors)? = ').strip().lower()
        p2_str = input(f'Enter {p2}, your choice (rock, paper, scissors)? = ').strip().lower()

        p_set = {"rock": 0, "paper": 1, "scissors": 2}
        rev_set = {0: "rock", 1: "paper", 2: "scissors"}

        you1 = p_set.get(p1_str)
        you2 = p_set.get(p2_str)

        if you1 is None or you2 is None:
            print("Invalid choices! Please choose rock, paper, or scissors.")
            continue

        print(f"\n{p1}, your choice is: {rev_set[you1]}")
        print(f"{p2}, your choice is: {rev_set[you2]}\n")

        if you1 == you2:
            print("It's a draw!")
        elif (you1 == 0 and you2 == 1) or (you1 == 1 and you2 == 2) or (you1 == 2 and you2 == 0):
            print(f"{p2} wins!")
        else:
            print(f"{p1} wins!")

    elif Players == 3:
        print("Ok! This game can be played with 3 players.")
        Ready2 = input("Are you ready to play the Rock, Paper, Scissors game? (Yes/No) = ")
        if Ready2.lower() != 'yes':
            print("Ok! Game closing...")
            break

        p1 = input("Enter player 1 name: ").strip()
        p2 = input("Enter player 2 name: ").strip()
        p3 = input("Enter player 3 name: ").strip()

        if not (p1.replace(" ", "").isalpha() and p2.replace(" ", "").isalpha() and p3.replace(" ", "").isalpha()):
            print("Please enter valid names for all players!")
            continue

        print('_____(GAME START!)_____')
        p1_str = input(f'Enter {p1}, your choice (rock, paper, scissors)? = ').strip().lower()
        p2_str = input(f'Enter {p2}, your choice (rock, paper, scissors)? = ').strip().lower()
        p3_str = input(f'Enter {p3}, your choice (rock, paper, scissors)? = ').strip().lower()

        rps = {"rock": 0, "paper": 1, "scissors": 2}
        rev = {0: "rock", 1: "paper", 2: "scissors"}

        you1 = rps.get(p1_str)
        you2 = rps.get(p2_str)
        you3 = rps.get(p3_str)

        if None in (you1, you2, you3):
            print("Invalid choices! Please choose rock, paper, or scissors.")
            continue

        print(f"\n{p1}, your choice is: {rev[you1]}")
        print(f"{p2}, your choice is: {rev[you2]}")
        print(f"{p3}, your choice is: {rev[you3]}\n")

        unique_choices = {you1, you2, you3}
        if len(unique_choices) == 1:
            print("It's a draw!")
        elif len(unique_choices) == 3:
            print("No one wins!")
        else:
            winners = []
            if you1 == you2 and (you1 - you3) % 3 == 1:
                winners = [p1, p2]
            elif you1 == you3 and (you1 - you2) % 3 == 1:
                winners = [p1, p3]
            elif you2 == you3 and (you2 - you1) % 3 == 1:
                winners = [p2, p3]
            elif (you1 - you2) % 3 == 1 and (you1 - you3) % 3 == 1:
                winners = [p1]
            elif (you2 - you1) % 3 == 1 and (you2 - you3) % 3 == 1:
                winners = [p2]
            elif (you3 - you1) % 3 == 1 and (you3 - you2) % 3 == 1:
                winners = [p3]
            if winners:
                print("Winner(s):", " and ".join(winners))

    else:
        print(f"This game can't be played with {Players} players!")

    replay = input("\nDo you want to play again? (Yes/No) = ")
    if replay.lower() != 'yes':
        print("Thanks for playing! Goodbye.")
        break
