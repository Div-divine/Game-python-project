import random
from my_project_pkg import techniques
from colorama import Fore, Back, Style

list_plants = [Fore.GREEN + "Scallions", Fore.GREEN + "Eggplants", Fore.GREEN + "Summer squash", Fore.RED + "Pepper",
               Fore.RED + "Strawberies", Fore.GREEN + "Thymes", Fore.GREEN + "Cucumbers", Fore.GREEN + "Lettuce", Fore.RED + "Tomatoes", Fore.GREEN + "Beans"]
best_place = [Fore.CYAN + "In pots,or containers!",
              Fore.YELLOW + "Directly outside in your garden!"]


def location_choice(list_plants, weather_sltd):
    print("The location choice you made for your",
          list_plants, "is:", weather_sltd)


def Lettuce_place(score):
    weather_sltd = random.choice(best_place)
    type = input("Type YES, to make a random selection.")
    if type == "yes":
        location_choice(list_plants[7], weather_sltd)

        if weather_sltd == best_place[0]:
            print("Congratulation,your",
                  list_plants[7], "is happy and waves at you", weather_sltd)
            x = 5
            score = score + x
            techniques.show_score(score)
            return score

        elif weather_sltd == best_place[1]:
            print("This is not the perfect place for your", list_plants[7])
            score -= 5
            techniques.show_score(score)
            return score

    elif type != "yes" or type == "":
        print("No selection made.")
        Lettuce_place(score)
        return score


def Tomatoes_place(score):
    weather_sltd = random.choice(best_place)
    type = input("Type YES, to make a random selection.")
    if type == "yes":
        location_choice(list_plants[8], weather_sltd)
        if weather_sltd == best_place[1]:
            print("Congratulation,your",
                  list_plants[8], "is happy and waves at you", weather_sltd)
            x = 5
            score = score + x
            techniques.show_score(score)
            return score

        elif weather_sltd == best_place[0]:
            print("This is not the perfect place for your", list_plants[8])
            score -= 5
            techniques.show_score(score)
            return score

    elif type != "yes" or type == "":
        print("No selection made.")
        Tomatoes_place(score)
        return score


def Beans_place(score):
    weather_sltd = random.choice(best_place)
    type = input("Type YES, to make a random selection.")
    if type == "yes":
        location_choice(list_plants[9], weather_sltd)

        if weather_sltd == best_place[1]:
            print("Congratulation,your",
                  list_plants[9], "is happy and waves at you", weather_sltd)
            x = 5
            score = score + x
            techniques.show_score(score)
            return score

        elif weather_sltd == best_place[0]:
            print("This is not the perfect place for your", list_plants[9])
            score -= 5
            techniques.show_score(score)
            return score

    elif type != "yes" or type == "":
        print("No selection made.")
        Beans_place(score)
        return score


def Scallions_place(score):
    weather_sltd = random.choice(best_place)
    type = input("Type YES, to make a random selection.")
    if type == "yes":
        location_choice(list_plants[0], weather_sltd)

        if weather_sltd == best_place[0]:
            print("Congratulation,your",
                  list_plants[0], "is happy and waves at you", weather_sltd)
            x = 5
            score = score + x
            techniques.show_score(score)
            return score

        elif weather_sltd == best_place[1]:
            print("This is not the perfect place for your", list_plants[0])
            score -= 5
            techniques.show_score(score)
            return score

    elif type != "yes" or type == "":
        print("No selection made.")
        Scallions_place(score)
        return score


def Eggplant_place(score):
    weather_sltd = random.choice(best_place)
    type = input("Type YES, to make a random selection.")
    if type == "yes":
        location_choice(list_plants[1], weather_sltd)

        if weather_sltd == best_place[0]:
            print("Congratulation,your",
                  list_plants[1], "is happy and waves at you", weather_sltd)
            x = 5
            score = score + x
            techniques.show_score(score)
            return score

        elif weather_sltd == best_place[1]:
            print("This is not the perfect place for your", list_plants[1])
            score -= 5
            techniques.show_score(score)
            return score

    elif type != "yes" or type == "":
        print("No selection made.")
        Eggplant_place(score)
        return score


def Summer_squash_place(score):
    weather_sltd = random.choice(best_place)
    type = input("Type YES, to make a random selection.")
    if type == "yes":
        location_choice(list_plants[2], weather_sltd)

        if weather_sltd == best_place[1]:
            print("Congratulation,your",
                  list_plants[2], "is happy and waves at you", weather_sltd)
            x = 5
            score = score + x
            techniques.show_score(score)
            return score

        elif weather_sltd == best_place[0]:
            print("This is not the perfect place for your", list_plants[2])
            score -= 5
            techniques.show_score(score)
            return score

    elif type != "yes" or type == "":
        print("No selection made.")
        Summer_squash_place(score)
        return score


def Pepper_place(score):
    weather_sltd = random.choice(best_place)
    type = input("Type YES, to make a random selection.")
    if type == "yes":
        location_choice(list_plants[3], weather_sltd)
        if weather_sltd == best_place[0]:
            print("Congratulation,your",
                  list_plants[3], "is happy and waves at you", weather_sltd)
            x = 5
            score = score + x
            techniques.show_score(score)
            return score

        elif weather_sltd == best_place[1]:
            print("This is not the perfect place for your", list_plants[3])
            score -= 5
            techniques.show_score(score)
            return score

    elif type != "yes" or type == "":
        print("No selection made.")
        Pepper_place(score)
        return score


def Strawberries_place(score):
    weather_sltd = random.choice(best_place)
    type = input("Type YES, to make a random selection.")
    if type == "yes":
        location_choice(list_plants[4], weather_sltd)
        if weather_sltd == best_place[1]:
            print("Congratulation,your",
                  list_plants[4], "is happy and waves at you", weather_sltd)
            x = 5
            score = score + x
            techniques.show_score(score)
            return score

        elif weather_sltd == best_place[0]:
            print("This is not the perfect place for your", list_plants[4])
            score -= 5
            techniques.show_score(score)
            return score

    elif type != "yes" or type == "":
        print("No selection made.")
        Strawberries_place(score)
        return score


def Thyme_place(score):
    weather_sltd = random.choice(best_place)
    type = input("Type YES, to make a random selection.")
    if type == "yes":
        location_choice(list_plants[5], weather_sltd)
        if weather_sltd == best_place[1]:
            print("Congratulation,your",
                  list_plants[5], "is happy and waves at you", weather_sltd)
            x = 5
            score = score + x
            techniques.show_score(score)
            return score

        elif weather_sltd == best_place[0]:
            print("This is not the perfect place for your", list_plants[5])
            score -= 5
            techniques.show_score(score)
            return score

    elif type != "yes" or type == "":
        print("No selection made.")
        Thyme_place(score)
        return score


def Cucumber_place(score):
    weather_sltd = random.choice(best_place)
    type = input("Type YES, to make a random selection.")
    if type == "yes":
        location_choice(list_plants[6], weather_sltd)
        if weather_sltd == best_place[1]:
            print("Congratulation,your",
                  list_plants[6], "is happy and waves at you", weather_sltd)
            x = 5
            score = score + x
            techniques.show_score(score)
            return score

        elif weather_sltd == best_place[0]:
            print("This is not the perfect place for your", list_plants[6])
            score -= 5
            techniques.show_score(score)
            return score

    elif type != "yes" or type == "":
        print("No selection made.")
        Cucumber_place(score)
        return score
