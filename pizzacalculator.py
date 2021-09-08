print ("dit is de pizzacalculator van roy otten")
print ("small pizza= 8")
print ("medium pizza= 11") 
print  ("large pizza = 16")

smallPrijs = 8
mediumPrijs = 11
largePrijs = 16

vraag= input ("welke grootte pizza wil je hebben?")
if vraag == ("small"):
    amountPizza = int(input("hoeveel pizza's wil je"))
    berekening = amountPizza * smallPrijs
    print("De afmeting die u heeft gekozen is: " + str(vraag) + " Het aantal is: " + str(amountPizza) + "Het bedrag is in totaal" + str(berekening))
elif vraag == ("medium"): 
    amountPizza = int(input("hoeveel pizza wil je hebben?"))
    berekening = amountPizza * mediumPrijs 
    print ("je afmeting die je gekozen hebt is: " + str(vraag) + " het aantal is: " + str(amountPizza) + "het bedrag is in totaal" + str(berekening))
elif vraag == ("large"):
    amountPizza = int(input("hoeveel pizza wil je hebben" )) 
    berekening = amountPizza * largePrijs
    print ("je afmeting die je gekozen hebt is: " + str(vraag) + " het aantal is: " + str(amountPizza) + "het bedrag is in totaal " + str(berekening))
print ("bedankt voor uw bestelling!!") 






