import random
from colorama import Fore, Back, Style

list_plants = [Fore.GREEN + "Scallions", Fore.GREEN + "Eggplants", Fore.GREEN + "Summer squash", Fore.RED + "Pepper",
               Fore.RED + "Strawberies", Fore.GREEN + "Thymes", Fore.GREEN + "Cucumbers", Fore.GREEN + "Lettuce", Fore.RED + "Tomatoes", Fore.GREEN + "Beans"]
best_weather = [Fore.GREEN+ Back.YELLOW + "warm soil",Fore.GREEN + Back.WHITE+ "cold soil"]


def show_score(score):
    print("Your current score is:", score, "Points")


def Lettuce(score):
    weather_sltd = random.choice(best_weather)
    type = input("Type YES, to make a random selection.")
    if type == "yes":
        print("The weather choice you made is:", weather_sltd)

        if weather_sltd == "cold soil":
            print("Congratulation,your",
                  list_plants[7], "is happy and waves at you from this", weather_sltd)
            x = 5
            score = score + x
            show_score(score)
            return score

        elif weather_sltd != "cold soil":
            print("This is not the perfect place for your", list_plants[7])
            score -= 5
            show_score(score)
            return score

    elif type != "yes" or type == "":
        print("No selection made.")
        Lettuce(score)
        return score


def Tomatoes(score):
    weather_sltd = random.choice(best_weather)
    type = input("Type YES, to make a random selection.")
    if type == "yes":
        print("The weather choice you made is:", weather_sltd)

        if weather_sltd == "warm soil":
            print(
                "Congratulation,your", list_plants[8], " plant is happy and waves at you from this", weather_sltd)
            score += 5
            show_score(score)
            return score

        elif weather_sltd != "warm soil":
            print("This is not the perfect place for your", list_plants[7])
            score -= 5
            show_score(score)
            return score


def Beans(score):
    weather_sltd = random.choice(best_weather)
    type = input("Type YES, to make a random selection.")
    if type == "yes":
        print("The weather choice you made is:", weather_sltd)
        if weather_sltd == "warm soil":
            print(
                "Congratulation,your", list_plants[9], " plant is happy and waves at you from this", weather_sltd)
            score += 5
            show_score(score)
            return score

        elif weather_sltd != "warm soil":
            print("This is not the perfect place for your", list_plants[7])
            score -= 5
            show_score(score)
            return score
    elif type != "yes" or type == "":
        print("No selection made.")
        Beans(score)


def Scallions(score):
    weather_sltd = random.choice(best_weather)
    type = input("Type YES, to make a random selection.")
    if type == "yes":
        print("The weather choice you made is:", weather_sltd)
        if weather_sltd == "warm soil":
            print(
                "Congratulation,your", list_plants[0], " plant is happy and waves to you in this", weather_sltd)
            score += 5
            show_score(score)
            return score

        elif weather_sltd != "warm soil":
            print("This is not the perfect place for your", list_plants[7])
            score -= 5
            show_score(score)
            return score
    elif type != "yes" or type == "":
        print("No selection made.")
        Scallions(score)


def Eggplant(score):
    weather_sltd = random.choice(best_weather)
    type = input("Type YES, to make a random selection.")
    if type == "yes":
        print("The weather choice you made is:", weather_sltd)
        if weather_sltd == "warm soil":
            print(
                "Congratulation,your", list_plants[1], " plant is happy and waves to you in this", weather_sltd)
            score += 5
            show_score(score)
            return score

        elif weather_sltd != "warm soil":
            print("This is not the perfect place for your", list_plants[7])
            score -= 5
            show_score(score)
            return score
    elif type != "yes" or type == "":
        print("No selection made.")
        Eggplant(score)


def Summer_squash(score):
    weather_sltd = random.choice(best_weather)
    type = input("Type YES, to make a random selection.")
    if type == "yes":
        print("The weather choice you made is:", weather_sltd)
        if weather_sltd == "warm soil":
            print(
                "Congratulation,your", list_plants[2], " plant is happy and waves to you in this", weather_sltd)
            score += 5
            show_score(score)
            return score

        elif weather_sltd != "warm soil":
            print("This is not the perfect place for your", list_plants[7])
            score -= 5
            show_score(score)
            return score
    elif type != "yes" or type == "":
        print("No selection made.")
        Summer_squash(score)


def Pepper(score):
    weather_sltd = random.choice(best_weather)
    type = input("Type YES, to make a random selection.")
    if type == "yes":
        print("The weather choice you made is:", weather_sltd)
        if weather_sltd == "warm soil":
            print(
                "Congratulation,your", list_plants[3], " plant is happy and waves to you in this", weather_sltd)
            score += 5
            show_score(score)
            return score

        elif weather_sltd != "warm soil":
            print("This is not the perfect place for your", list_plants[7])
            score -= 5
            show_score(score)
            return score
    elif type != "yes" or type == "":
        print("No selection made.")
        Pepper(score)


def Strawberries(score):
    weather_sltd = random.choice(best_weather)
    type = input("Type YES, to make a random selection.")
    if type == "yes":
        print("The weather choice you made is:", weather_sltd)
        if weather_sltd == "cold soil":
            print(
                "Congratulation,your", list_plants[4], " plant is happy and waves to you in this", weather_sltd)
            score += 5
            show_score(score)
            return score

        elif weather_sltd != "cold soil":
            print("This is not the perfect place for your", list_plants[4])
            score -= 5
            show_score(score)
    elif type != "yes" or type == "":
        print("No selection made.")
        Strawberries(score)


def Thymes(score):
    weather_sltd = random.choice(best_weather)
    type = input("Type YES, to make a random selection.")
    if type == "yes":
        print("The weather choice you made is:", weather_sltd)
        if weather_sltd == "warm soil" or weather_sltd == "cold soil":
            print("Congratulation,your",
                  list_plants[5], " plant is happy and waves to you in this", weather_sltd)
            print("Your plant can grow both in",
                  best_weather[0], "and in", best_weather[1])
            show_score(score)
            return score

    elif type != "yes" or type == "":
        print("No selection made.")
        Thymes(score)


def Cucumbers(score):
    weather_sltd = random.choice(best_weather)
    type = input("Type YES, to make a random selection.")
    if type == "yes":
        print("The weather choice you made is:", weather_sltd)
        if weather_sltd == "warm soil":
            print(
                "Congratulation,your", list_plants[6], " plant is happy and waves to you in this", weather_sltd)
            score += 5
            show_score(score)
            return score

        elif weather_sltd != "warm soil":
            print("This is not the perfect place for your", list_plants[6])
            score -= 5
            show_score(score)
            return score
    elif type != "yes" or type == "":
        print("No selection made.")
        Cucumbers(score)


def ext_game(score):
    print("LEAVING......")
    print("GoodBye, SEE YOU SOON!")
    show_score(score)

    return score
