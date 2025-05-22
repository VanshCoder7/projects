
print('\n')
Players = input("Hello,\nHow many player want to play (rock,paper,scissors) game? = ")
if (int(Players)<=0):
    print("Invaild import!")

elif (int(Players)==1):
    print("This game can't play solo!")

elif (int(Players)==2):
    print('Ok!, This game can play two players.')
    Ready = input("Are you ready to play (rock,paper,scissors) game?(Yes/No) = ")
    if Ready == 'Yes' or 'yes':
        p1 = input("Enter player 1 name : ")
        p2 = input("Enter player 2 name : ")
        if p1.isalpha():
            if p2.isalpha():
                print('_____(GAME)_____')
                p1_str = input(f'Enter {p1} your choice (rock,paper,scissors)? = ')
                p2_str = input(f'Enter {p2} your choice (rock,paper,scissors)? = ')
                p1_set = {"rock":0, "paper":1, "scissors":2}
                p1_revesedset = {0:"rock", 1:"paper", 2:"scissors"}
                p2_set = {"rock":0, "paper":1, "scissors":2}
                p2_revesedset = {0:"rock", 1:"paper", 2:"scissors"}

                you1 = p1_set[p1_str]
                you2 = p2_set[p2_str]

                print('')
                print(f"{p1} your choive is : {p1_revesedset[you1]}")
                print(f"{p2} your choive is : {p2_revesedset[you2]}")
                print('')

                if (you1 == you2):
                    print("It's drow!")

                elif (you1 == 0 and you2 == 1):
                    print(f"{p2} is Win!")

                elif (you1 == 0 and you2 == 2):
                    print(f"{p1} is Win!")

                elif (you1 == 1 and you2 == 0):
                    print(f"{p1} is Win!")

                elif (you1 == 1 and you2 == 2):
                    print(f"{p2} is Win!")

                elif (you1 == 2 and you2 == 0):
                    print(f"{p2} is Win!")

                elif (you1 == 2 and you2 == 1):
                    print(f"{p1} is Win!")
            
            else:
                print(f"Enter {p2} vaild input!")
        
        else:
            print(f"Enter {p1} vaild input!")

    else:
        print("Ok!, Game closing...")        