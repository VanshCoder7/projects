import random

# Bus Station like first print where you go print name all station you want go you check where you want to go and print that program give him location with priaces.

BRTS_Station_Sarthana_List = { 
'Sarthana main'  : 20, 
'Udhna'  : 25, 
'Varachha'  : 30, 
'Kapodra'  : 40, 
'Kamrej'  : 50, 
'Adajan'  : 55, 
'Parle Point'  : 60, 
'Athwagate'  : 65, 
'Bhestan'  : 70, 
'Dindoli'  : 75, 
'Puna Gam'  : 80, 
'Katargam'  : 85, 
'Vesu'  : 90, 
'Pal'  : 95, 
'ONGC Nagar'  : 100, 
}

Bus_Number = random.randint(1,500)

Station_price = 0

print("\nHere All List of BRTS Station.\n1.Sarthana main  \n2.Udhna  \n3.Varachha  \n4.Kapodra  \n5.Kamrej  \n6.Adajan  \n7.Parle Point \n8.Athwagate  \n9.Bhestan  \n10.Dindoli  \n11.Puna Gam  \n12.Katargam  \n13.Vesu  \n14.Pal  \n15.ONGC Nagar")

Station_Want1  = input("Which Station You Want to go = ")
if Station_Want1 in BRTS_Station_Sarthana_List:
    Station_price += BRTS_Station_Sarthana_List[Station_Want1]
    print(f"Your {Station_Want1} Station is Avaliable to go.")
    print(f"Your {Station_Want1} Station Price {Station_price}Rs")   
    print(f"You go Bus Number {Bus_Number}")    
else:
    print(f"Your {Station_Want1} Station Not Avaliable in BRTS!\n")
    Station_Want2 = input("I give you reList You want to go in this list.(Yes/No) :")
    if Station_Want2 == 'Yes':
        print("\nHere All List of BRTS Station.\n1.Sarthana main  \n2.Udhna  \n3.Varachha  \n4.Kapodra  \n5.Kamrej  \n6.Adajan  \n7.Parle Point \n8.Athwagate  \n9.Bhestan  \n10.Dindoli  \n11.Puna Gam  \n12.Katargam  \n13.Vesu  \n14.Pal  \n15.ONGC Nagar")
        Station_Want2 = input("Which Station You Want to go = ")
        if Station_Want2 in BRTS_Station_Sarthana_List:
            Station_price += BRTS_Station_Sarthana_List[Station_Want2] 
            print(f"Your {Station_Want2} Station is Avaliable to go.")
            print(f"Your {Station_Want2} Station Price {Station_price}Rs")   
            print(f"You go Bus Number {Bus_Number}")    
        else:
            print(f"Your {Station_Want2} Station Not Avaliable in BRTS!\n")
    else:
        print("Ok Bhai Good Bye!")        