# print(2 ** 179)
# print("This is a number:", 125)
# n = 2.777
# print(str(float(int(n))))

# print("Give me ur number!")
# num_1 = int(input())  # put your python code here
# num_1 %= 10
# print(num_1)

# class_1 = abs(int(input()))
# class_2 = abs(int(input()))
# class_3 = abs(int(input()))

# desk = 0

# desk += class_1 // 2 + class_1 % 2
# desk += class_2 // 2 + class_2 % 2
# desk += class_3 // 2 + class_3 % 2

# print(desk)



# # Save the input in this variable
# ticket = input()

# # Add up the digits for each half
# half1 = ticket[0] + ticket[1] + ticket[2]
# half2 = ticket[3] + ticket[4] + ticket [5]

# # Thanks to you, this code will work
# if half1 == half2:
#     print("Lucky")
# else:
#     print("Ordinary")



# print("How many cups of coffee u will need: ")
# cups = int(input())
# watr = cups * 200
# milk = cups * 50
# beans = cups * 15


# print("For " + str(cups) + " cups of coffee u wil need: ")
# print(str(watr) + " ml of water")
# print(str(milk) + " ml of milk")
# print(str(beans) + " g of coffee beans")


# COFFEE MACHINE




# print("Write how many ml of water the coffee machine has: ")
# water = int(input())
# print("Write how many ml of milk the coffee machine has: ")
# milk = int(input())
# print("Write how many grams of coffee beans the coffee machine has: ")
# beans = int(input())
# print("How many cups of coffee u will need: ")
# cups_request = int(input())

# cups_available = min(water // 200, milk // 50, beans // 15)

# if cups_request == cups_available:
#     print("Yes, I can make that amount of coffee")
# elif cups_request > cups_available:
#     print("No, I can make only " + str(cups_available) + " cups of coffee")
# else:
#     print("Yes, I can make that amount of coffee (and even " 
#     + str((cups_available - cups_request)) + " more than that")






# print("For " + str(cups) + " cups of coffee u wil need: ")
# print(str(watr) + " ml of water")
# print(str(milk) + " ml of milk")
# print(str(beans) + " g of coffee beans")


# print("Starting to make a coffee")
# print("Grinding coffee beans")
# print("Boiling water")
# print("Mixing boiled water with crushed coffee beans")
# print("Pouring coffee into the cup")
# print("Pouring some milk into the cup")
# print("Coffee is ready!")


money = 550
water = 400
milk = 540
c_beans = 120
cups = 9


def supplies(water, milk, coffee_beans, cups, money):
    print("The coffee machine has: ")
    print(str(water) + " of water")
    print(str(milk) + " of milk")
    print(str(coffee_beans) + " of coffee beans")
    print(str(cups) + " of disposable cups")
    print(str(money) + " of money")

def not_enough(rem_supply, requested_supply):
    if rem_supply < requested_supply:
        return 1
    else:
        return 0


# supplies(water, milk, c_beans, cups, money)
while True:
    print("Welcome! Write down what do you want to do (buy, fill, take, reamining, exit): ")
    action = input()

    if action == "buy":
        print("What do you want to buy? Press 1 for espresso, 2 for latte and 3 for cappuccino or back to main menu:")
        coffee_type = input()
        if coffee_type == "1":
            if not_enough(water, 250) == 1:
                print("Sorry, not enough water!")
            elif not_enough(c_beans, 16) == 1:
                print("Sorry, not enough coffee beans!")
            elif not_enough(cups, 1) == 1:
                print("Sorry, not enough cups!")
            else:
                print("I have enough resources, making you coffee!")
                #supplies(water - 250, milk, c_beans - 16, cups - 1, money + 4)
                water -= 250
                c_beans -= 16
                cups -= 1
                money += 4
        elif coffee_type == "2":
            if not_enough(water, 350) == 1:
                print("Sorry, not enough water!")
            elif not_enough(milk, 75) == 1:
                print("Sorry, not enough milk!")
            elif not_enough(c_beans, 20) == 1:
                print("Sorry, not enough coffee beans!")
            elif not_enough(cups, 1) == 1:
                print("Sorry, not enough cups!")
            else:
                print("I have enough resources, making you coffee!")
                #supplies(water - 350, milk - 75, c_beans - 20, cups - 1, money + 7)
                water -= 350
                milk -= 75
                c_beans -= 20
                cups -= 1
                money += 7
        elif coffee_type == "3":
            if not_enough(water, 200) == 1:
                print("Sorry, not enough water!")
            elif not_enough(milk, 100) == 1:
                print("Sorry, not enough milk!")
            elif not_enough(c_beans, 12) == 1:
                print("Sorry, not enough coffee beans!")
            elif not_enough(cups, 1) == 1:
                print("Sorry, not enough cups!")
            else:
                print("I have enough resources, making you coffee!")
                #supplies(water - 200, milk - 100, c_beans - 12, cups - 1, money + 6)
                water -= 200
                milk -= 100
                c_beans -= 12
                cups -= 1
                money += 6
        elif "back":
            continue
        else:
            print("No coffee type for " + str(coffee_type) + " number")



    elif action == "fill":
        print("Write how many ml of water do you want to add: ")
        inp_water = int(input())
        print("Write how many ml of milk do you want to add: ")
        inp_milk = int(input())
        print("Write how many grams of coffee beans do you want to add: ")
        inp_beans = int(input())
        print("Write how many disposable cups of coffee do you want to add: ")
        inp_cups = int(input())

        supplies(water + inp_water, milk + inp_milk, c_beans + inp_beans, cups + inp_cups, money)
        water += inp_water
        milk += inp_milk
        c_beans += inp_beans
        cups += inp_cups


    elif action == "take":
        print("I gave you $" + str(money))
        #supplies(water, milk, c_beans, cups, money - money)
        money -= money

    elif action == "remaining":
        supplies(water, milk, c_beans, cups, money)
    elif action == "exit":
        break



































