"""Write a line of code that creates a LIST object of 5 elements/items. Label the variable 'fruit',
likewise, each element/item should be a fruit."""
#code here
Fruit = ['apple', 'pear', 'watermelon', 'tomato', 'orange']
print(Fruit)
"""After doing that, remove/pop() off the third item of that list and store it in a variable labeled 'badFruit'"""
#code here
badFruit = Fruit.pop(2)
print(badFruit)
"""Add/append() a new fruit to your fruit list."""
#code here
Fruit.append('banana')
print(Fruit)

"""How many fruits do you have in your fruit list? print a pretty message.
ex. print('There are {0} fruit in the fruit list".format(len(fruitList)))"""
#code here

print("Hello David, your number of items in your list is : {0}".format(len(Fruit)))

#########################################################################
# New Exercise
#########################################################################
"""Reassign string value 'David' to say YOUR ACTUAL NAME."""
# ex. of reassignment - list0[3] = 'Your Name'

list1 = [1,2,['David']] #1
#code here
list1[2] = 'Miguel'
print(list1)

list2 = [1,2,[3,4,'David']] #2
#code here
list2[2][2] = 'Miguel'
print(list2)

list3 = [1,2,[3,6],[2,'David']] #3
#code here
list3[3][1] = 'Miguel'
print(list3)
############################################################
# New exercise
############################################################


"""Use keys to grab hello from the follow dictionaries:"""
#Remember dictionaries are key/value pairs. To identify the value we need
#to provide the key.
#ex. d = {'key1':'val1','key2':'val2'}
# d['key2']
#>>> 'val2'

d = {'simple_key':'hello'} #1
d['simple_key']

d = {'k1': 1,'k2':2,'k3':'hello'} #2
d['k3']

d = {'k1': 1,'k2':[1,2,3,'hello'],'k3':3} #3
d = d['k2'][3]

"""Image we are working for a resturant business. One of our responsibilites is to keep
track of the inventory. The next few lines of code will be a scenario we need to code out line by line"""


"""We received a bulk shipment of fruit. Create a dictionary of 15 bananas, 25 apples, and 10 pears.
Store the dictionary in a variable called inventory."""
#code here

inventory = {'bananas': 15,'apples': 25,'pears' : 10}
print(inventory)
"""Someone just purchased 5 apples. Update the dictionary to reflect those changes."""
#code here
inventory['apples']=20
print(inventory)

"""We now have a new vendor and they've provided us with 30 oranges. Update our inventory to reflect these changes"""
#code here
inventory['oranges'] = 30
print(inventory)

"""I ate 5 oranges; update the inventory"""
#code here

inventory['oranges'] = 25
print(inventory)
"""all of the pears were sold. update the inventory"""
#code here

inventory['pears'] = 0
print(inventory)
"""We ran out of pears and not longer need to keep track of it's inventory. Delete/remove pears from our inventory."""
#code here

del inventory['pears']
print(inventory)





