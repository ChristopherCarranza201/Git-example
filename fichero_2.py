import random
list = ["apple" , "pear" , "strawberry"]
num_fruit = len(list)
random_choice = random.randint(0, num_fruit -1)
chosen_fruit = list[random_choice]
print(chosen_fruit)

