def highRiskLevels(price, money):
    print("{} shares at {}".format(round(risk_money/spread + 0.01, 2), round(spread + 0.01, 2)))
    print("{} shares at {}".format(round(risk_money/spread + 0.02, 2), round(spread + 0.02, 2)))
    print("{} shares at {}".format(round(risk_money/spread + 0.03, 2), round(spread + 0.03, 2)))
    print("{} shares at {}".format(round(risk_money/spread + 0.04, 2), round(spread + 0.04, 2)))
    print("{} shares at {}\n".format(round(risk_money/spread + 0.05, 2), round(spread + 0.05, 2)))

loop = True
while loop == True:
    risk_price = float(input("Risk Level Price: "))
    #print("You entered: {}".format(risk_price))
    #print("Type: {}".format(type(risk_price)))

    buy_price = float(input("Target Buy Price: "))
    #print("You entered: {}".format(buy_price))

    #Calculate the risk spread
    spread = buy_price - risk_price
    #print("Spread: "+ str(spread))

    risk_money = float(input("How much to risk?: "))
    #print("You entered: {}".format(risk_money))

    print("\nYou can buy {} shares\n".format(round(risk_money/spread)))
    highRiskLevels(risk_price, risk_money)
    print("----------------------\n")

    another = input("Another? y/n\n")
    if another.lower() == "y":
        loop = True
        print("----------------------\n")
    else:
        loop = False
        quit()

        
