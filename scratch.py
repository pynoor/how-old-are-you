while True :
    try :
            age = int(input("How old are you? ..."))
    except ValueError :
            print ("Sorry, I don't get that!")
            continue
    while age < 13 :
        print ("You're way too young to drink Raki...")
        print("Play again when you're older !")
        age = int(input("How old are you? ..."))
    if age == 13 :
        print ("Congratulations, you can now have your first Raki!")
        print("Play again...")
    elif age == 14 :
        print ("You've probably already drank your first Raki now. Tastes good, eh? Side note : Raki is also popular in Turkey, Greece and Iran!")
        print("Play again...")
    elif age == 15 :
        print ("Don't let the Raki take over your life, now is a good time to set some limits! Remember, this stuff has 40-50% Alcohol in it!")
        print("Play again...")
    elif age == 16 :
        print ("In Turkey, drinking Raki on your own is a sign of loneliness. Get some friends to drink with you!")
        print("Play again...")
    elif age == 17 :
        print ("Don't drink and drive ! :P")
        print ("Play again...")
    elif age < 100 :
        print("You're a rakixpert!")
        print("Play again...")
    elif age >= 100 :
        if age == 1000 :
              break
        elif age != 1000 :
            print ("You're too old to drink Raki !")
            break
print ("See you next time!")
