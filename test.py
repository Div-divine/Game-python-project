import random


def num():

    rnd_num = random.randint(1, 10)
    print(rnd_num)

    if rnd_num <= 4:
        print("You are not half way close!")

    elif rnd_num == 5:
        print("You are half way close!")

    elif rnd_num > 5:
        print("Congratulation, you have gone far enough!")


# num()
list_plants = ["Scallions", "Eggplants", "Summer squash", "Pepper",
               "Strawberies", "Thymes", "Cucumbers", "Lettuce", "Tomatoes", "Beans"]


def try_choice(x, y, list_plants):
    print("best time for", list_plants, "is", x, "till", y)


try_choice(2, 5, list_plants[2])
