
print('\n')
Players = input("Hello,\nHow many player want to play (rock,paper,scissors) game? = ")
if (int(Players)<=0):
    print("Invaild import!")

elif (int(Players)==1):
    print("This game can't play solo!")

elif (int(Players)==2):
    print('Ok!, This game can play two players.')
    Ready = input("Are you ready to play (rock,paper,scissors) game? (Yes/No) = ")
    if Ready == 'Yes':
        p1 = input("Enter player 1 name : ")
        p2 = input("Enter player 2 name : ")
        if p1.isalpha():
            if p2.isalpha():
                print('_____(GAME START!)_____')
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

elif (int(Players)==3):
    print("Ok!, This game play 3 players. ")
    Ready2 = input("Are you ready to play (rock,paper,scissors) game? (Yes/No)  = ")
    if Ready2 == 'Yes':
        p1 = input("Enter player 1 name : ")
        p2 = input("Enter player 2 name : ")
        p3 = input("Enter player 3 name : ")
        if p1.isalpha():
            if p2.isalpha():
                if p3.isalpha():
                    print('_____(GAME START!)_____')
                    p1_str = input(f'Enter {p1} your choice (rock,paper,scissors)? = ')
                    p2_str = input(f'Enter {p2} your choice (rock,paper,scissors)? = ')
                    p3_str = input(f'Enter {p3} your choice (rock,paper,scissors)? = ')
                    p1_set = {"rock":0, "paper":1, "scissors":2}
                    p1_revesedset = {0:"rock", 1:"paper", 2:"scissors"}
                    p2_set = {"rock":0, "paper":1, "scissors":2}
                    p2_revesedset = {0:"rock", 1:"paper", 2:"scissors"}
                    p3_set = {"rock":0, "paper":1, "scissors":2}
                    p3_revesedset = {0:"rock", 1:"paper", 2:"scissors"}

                    you1 = p1_set[p1_str]
                    you2 = p2_set[p2_str]    
                    you3 = p3_set[p3_str]

                    print('')    
                    print(f"{p1} your choive is : {p1_revesedset[you1]}")
                    print(f"{p2} your choive is : {p2_revesedset[you2]}")
                    print(f"{p3} your choive is : {p3_revesedset[you3]}")
                    print('')    

                    if (you1 == you2 == you3):
                        print("I's drow!")
# 0
                    elif (you1 == 0 and you2 == 1 and you3 == 2):
                        print(f"Noo any Win!")
                
                    elif (you1 == 0 and you2 == 2 and you3 == 1):
                        print(f"Noo any Win!")
                    
                    elif (you1 == 0 and you2 == 1 and you3 == 1):
                        print(f"{p2} and {p3} is Win!")
                   
                    elif (you1 == 0 and you2 == 2 and you3 == 2):
                        print(f"{p1} is Win!")
 
# 1
                    elif (you1 == 1 and you2 == 2 and you3 == 0):
                        print(f"Noo any Win!")
                
                    elif (you1 == 1 and you2 == 0 and you3 == 2):
                        print(f"Noo any Win!")
                    
                    elif (you1 == 1 and you2 == 0 and you3 == 0):
                        print(f"{p1} is Win!")
                   
                    elif (you1 == 1 and you2 == 2 and you3 == 2):
                        print(f"{p2} and {p3} is Win!")
# 2
                    elif (you1 == 2 and you2 == 1 and you3 == 0):
                        print(f"Noo any Win!")
                
                    elif (you1 == 2 and you2 == 0 and you3 == 1):
                        print(f"Noo any Win!")
                    
                    elif (you1 == 2 and you2 == 0 and you3 == 0):
                        print(f"{p2} and {p3} is Win!")
                   
                    elif (you1 == 2 and you2 == 1 and you3 == 1):
                        print(f"{p1} is Win!")

                else:
                    print(f"Enter {p3} vaild input!")
            else:
                print(f"Enter {p2} vaild input!")
        else:
            print(f"Enter {p1} vaild input!")
    
    else:
        print("Ok!, Game closing...")    