from random import randint


n=1
while n<=13:
    god_rojdenia = randint(1991,2022)


    start = 1990
    #god_rojdenia = int(input("Vvedite god rojdenia - "))


    if god_rojdenia <=1990 or god_rojdenia >=2022:
        print("nesootvestvuet usloviam zaadaci")
    else:
        goda= god_rojdenia-start
        if goda >0 and goda<=3:
            print("Baby -", goda, "years." )
        elif goda>3 and goda<=9:
            print("Kid -",goda,"years.")
        elif goda>9 and goda<=15:
            print("Teen -",goda,"years.")
        elif goda>15 and goda<=18:
            print("Yong -",goda,"years.")
        else: 
            goda>18 and goda<=31
            print("Old -",goda,"years.")
    n+=1