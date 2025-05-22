
#shop phone and headphone.

Phones_in_Shop_List = {
    'Apple iPhone 15' : 61900,
    'Apple iPhone 15 Pro Max' : 149900,
    'Apple iPhone 15 Pro' : 129900,
    'Samsung Galaxy A15 5G' : 15345,
    'Samsung Galaxy A15 4G' : 14998,
    'Samsung Galaxy A05' : 12999,
    'Redmi 13C 4G' : 7699,
    'Samsung Galaxy A35' : 22725,
    'iPhone 14' : 74900,
    'Samsung Galaxy S24' : 114999,
}

HeadPhones_in_Shop_List = {
    'Sony WH-1000XM5': 34999,
    'Bose QuietComfort 45': 32999,
    'Apple AirPods Max': 59900,
    'Sennheiser Momentum 4': 25990,
    'JBL Tour One M2': 17999,
    'Bang & Olufsen Beoplay H95': 99000,
    'Sony WH-CH720N': 11999,
    'Shure AONIC 50': 34000,
    'Anker Soundcore Life Q35' : 9999,
    'boAt Nirvanaa 751 ANC':  3799,
}


print('')
print("Hello Sir!\n     Welcome to My Shop I have Available Phones and Headphones.")
print("Here List of all Phones and Headphones With his Price.\n")
print("Phones List.\nApple iPhone 15 : 61900Rs\nApple iPhone 15 Pro Max : 149900Rs\nApple iPhone 15 Pro : 129900Rs\nSamsung Galaxy A15 5G : 15345Rs\nSamsung Galaxy A15 4G : 14998Rs\nSamsung Galaxy A05 : 12999RS\nRedmi 13C 4G : 7699RS\nSamsung Galaxy A35 : 22725Rs\niPhone 14 : 74900RS\nSamsung Galaxy S24 : 114999RS\n")
print("Headphones List.\nSony WH-1000XM5 : 34999Rs\nBose QuietComfort 45 : 32999Rs\nApple AirPods Max : 59900Rs\nSennheiser Momentum 4 : 25990Rs\nJBL Tour One M2 : 17999Rs\nBang & Olufsen Beoplay H95 : 99000Rs\nSony WH-CH720N : 11999Rs\nShure AONIC 50 : 34000Rs\nAnker Soundcore Life Q35  : 9999Rs\nboAt Nirvanaa 751 ANC :  3799Rs\n")
print('')

Total_Order_Phones = 0
Total_Order_Headphones = 0
Want1_Phone = input("Enter Phone name You want :")
if Want1_Phone in Phones_in_Shop_List:
    Total_Order_Phones += Phones_in_Shop_List[Want1_Phone] 
    print("Your Phone is Added.")
    Want2_Phone = input("You want more Phone? (Yes/No) :")
    if Want2_Phone == 'Yes':
        Want2_Phone = input("Enter Your Second Phone name You want :")
        if Want2_Phone in Phones_in_Shop_List:
            Total_Order_Phones += Phones_in_Shop_List[Want2_Phone] 
            print("Your Phone is Added.")
            print(f"Ok Your Fianl Amount of Phone is {Total_Order_Phones}Rs")
        else:
            print(f"This {Want2_Phone} Phone Not available yet.")
    else:
        print(f"Ok Your Fianl Amount of Phone is {Total_Order_Phones}Rs")
else:
    print(f"This {Want1_Phone} Phone Not available yet.")


Want3_Headphone = input("You want Headphones? (Yes/No) :")
if Want3_Headphone == 'Yes':
    Want3_Headphone = input("Enter Headphones name You want :")
    if Want3_Headphone in HeadPhones_in_Shop_List:
        Total_Order_Headphones += HeadPhones_in_Shop_List[Want3_Headphone] 
        print("Your Headphone is Added.")
        Want4_Headphone = input("You want more Headphone. (Yes/No) :")
        if Want4_Headphone == 'Yes':
            Want4_Headphone = input("Enter Your Second Headphone name You want :")
            if Want4_Headphone in HeadPhones_in_Shop_List:
                Total_Order_Headphones += HeadPhones_in_Shop_List[Want4_Headphone] 
                print("Your Headphone is Added.")
                print(f"Ok Your Fianl Amount of Headphone is {Total_Order_Headphones}Rs")    
            else:
                print(f"This {Want4_Headphone} Headphone is Not available yet.")
        else:
            print(f"Ok Your Fianl Amount of Headphone is {Total_Order_Headphones}Rs")        

    else:
        print(f"This {Want3_Headphone} is Not available yet.")    
        
else:
    print("Ok Thank You Sir! Nice to Meet You.")




print(f"Your total purchase is : {Total_Order_Phones+Total_Order_Headphones}Rs ")
