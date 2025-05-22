
manu_Fruits = {
        'Apple': 20,
        'Banana': 15,
        'Mango': 25,
        'Orange':30,
        'Grapes':20,
        'Pineapple':70,
        'Papaya':50,
        'Watermelon':60,
        'Strawberry':55,
        'Kiwi':45,   
}  


Total_Order_Fruits = 0
print('')
print("Welcome to My Fruit Restaurant Sir!")
print("Here manu of Fruits.\n\nApple: 20Rs\nBanana:15Rs\nMango: 25Rs\nOrange: 30Rs\nGrapes: 20Rs\nPineapple: 70Rs\nPapaya: 50Rs\nWatermelon: 60Rs\nStrawberry: 55Rs\nKiwi: 45Rs\n")
Fruit1 = input("Enter Fruit You Want :")
if Fruit1 in manu_Fruits:
    Total_Order_Fruits += manu_Fruits[Fruit1]
    print("Your Fruit added.")
else:
    print(f"Your Fruit {Fruit1} is Not Available Yet!")    

Want2 = input("You want to by more Fruits! (Yes/No) :")
if Want2 == 'Yes':
    Fruit2 = input("Enter Fruit You Want Next:")
    if Fruit2 in manu_Fruits:
        Total_Order_Fruits += manu_Fruits[Fruit2]
        print("Your Fruit added.")
else:
    print(f"Ok Sir. Yours Final Amount of is :{Total_Order_Fruits}Rs")        
    print('')

print(f"Ok Sir Yours Final Amount of is :{Total_Order_Fruits}Rs")        
print('')