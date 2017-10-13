
while True :
    try :
            age = int(input("How old are you? ..."))
    except ValueError :
            print ("Sorry, I don't get that!")
            continue
    while age < 13 :
        print ("You're too young to drink Raki")
        print("Play again...")
        age = int(input("How old are you? ..."))
    if age == 13 :
        print ("Congratulations, you can now have your first Raki!")
        print("Play again...")
    elif age == 14 :
        print ("You've probably already drank your first Raki now. Tastes good, eh?")
        print("Play again...")
    elif age == 15 :
        print ("Don't let the Raki take over your life, now is a good time to set some limits!")
        print("Play again...")
    elif age == 16 :
        print ("A tip : Don't hide the Raki under your cushions ... it smells !")
        print("Play again...")
    elif age == 17 :
        print ("How many Rakis can you drink in a minute ?")
        print ("Play again...")
    elif age >= 18 :
         if age == 1000:
              break
         elif age != 1000 :
              print ("You're a rakixpert!")
              print("Play again...")
print ("See you next time!")
