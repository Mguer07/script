import random
min = 1
max = 12

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print ("Rolling the dices")
    print ("The values are....")
    print ("person 1:",random.randint(min, max))
    print ("person 2:",random.randint(min, max))

    roll_again = input("Roll the dices again?")
