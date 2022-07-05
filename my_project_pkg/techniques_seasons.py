import random
from colorama import Fore, Back, Style
from my_project_pkg import techniques

best_season = [Fore.YELLOW + "Summer", "Spring", "Autumn", "Winter"]
list_plants = [Fore.GREEN + "Scallions", Fore.GREEN + "Eggplants", Fore.GREEN + "Summer squash", Fore.RED + "Pepper",
               Fore.RED + "Strawberies", Fore.GREEN + "Thymes", Fore.GREEN + "Cucumbers", Fore.GREEN + "Lettuce", Fore.RED + "Tomatoes", Fore.GREEN + "Beans"]


def season(list_plants, best_season):
    print("Your", list_plants, "grows better in", best_season)


def Lettuce_season(score):
    weather_sltd = random.choice(best_season)
    season(list_plants[7], best_season[1])
    type = input("Type YES, to make a random selection.")
    if type == "yes":
        print("The season choice you made is:", weather_sltd)

        if weather_sltd == "Spring":
            print("Congratulation,your", list_plants,
                  "is happy and waves at you from this", weather_sltd)
            x = 5
            score = score + x
            techniques.show_score(score)
            return score

        elif weather_sltd != "Spring":
            print("This is not the perfect season for your", list_plants[7])
            score -= 5
            techniques.show_score(score)
            return score

    elif type != "yes" or type == "":
        print("No selection made.")
        Lettuce_season(score)
        return score


def Tomatoes_season(score):
    weather_sltd = random.choice(best_season)
    season(list_plants[8], best_season[0])
    type = input("Type YES, to make a random selection.")
    if type == "yes":
        print("The season choice you made is:", weather_sltd)

        if weather_sltd == "Summer":
            print("Congratulation,your",
                  list_plants[8], "is happy and waves at you from this", weather_sltd)
            x = 5
            score = score + x
            techniques.show_score(score)
            return score

        elif weather_sltd != "Summer":
            print("This is not the perfect season for your", list_plants[8])
            score -= 5
            techniques.show_score(score)
            return score

    elif type != "yes" or type == "":
        print("No selection made.")
        Tomatoes_season(score)
        return score


def Beans_season(score):
    weather_sltd = random.choice(best_season)
    season(list_plants[9], best_season[1])
    type = input("Type YES, to make a random selection.")
    if type == "yes":
        print("The season choice you made is:", weather_sltd)

        if weather_sltd == "Spring":
            print("Congratulation,your",
                  list_plants[9], "is happy and waves at you from this", weather_sltd)
            x = 5
            score = score + x
            techniques.show_score(score)
            return score

        elif weather_sltd != "Spring":
            print("This is not the perfect season for your", list_plants[9])
            score -= 5
            techniques.show_score(score)
            return score

    elif type != "yes" or type == "":
        print("No selection made.")
        Beans_season(score)
        return score


def Scallions_season(score):
    weather_sltd = random.choice(best_season)
    season(list_plants[0], best_season[1])
    type = input("Type YES, to make a random selection.")
    if type == "yes":
        print("The season choice you made is:", weather_sltd)

        if weather_sltd == "Spring":
            print("Congratulation,your",
                  list_plants[0], "is happy and waves at you from this", weather_sltd)
            x = 5
            score = score + x
            techniques.show_score(score)
            return score

        elif weather_sltd != "Spring":
            print("This is not the perfect place for your", list_plants[0])
            score -= 5
            techniques.show_score(score)
            return score

    elif type != "yes" or type == "":
        print("No selection made.")
        Scallions_season(score)
        return score


def Eggplant_season(score):
    weather_sltd = random.choice(best_season)
    season(list_plants[1], best_season[0])
    type = input("Type YES, to make a random selection.")
    if type == "yes":
        print("The season choice you made is:", weather_sltd)

        if weather_sltd == "Summer":
            print("Congratulation,your",
                  list_plants[1], "is happy and waves at you from this", weather_sltd)
            x = 5
            score = score + x
            techniques.show_score(score)
            return score

        elif weather_sltd != "Summer":
            print("This is not the perfect place for your", list_plants[1])
            score -= 5
            techniques.show_score(score)
            return score

    elif type != "yes" or type == "":
        print("No selection made.")
        Eggplant_season(score)
        return score


def Summer_squash_season(score):
    weather_sltd = random.choice(best_season)
    season(list_plants[2], best_season[1])
    type = input("Type YES, to make a random selection.")
    if type == "yes":
        print("The season choice you made is:", weather_sltd)

        if weather_sltd == "Spring":
            print("Congratulation,your",
                  list_plants[2], "is happy and waves at you from this", weather_sltd)
            x = 5
            score = score + x
            techniques.show_score(score)
            return score

        elif weather_sltd != "Spring":
            print("This is not the perfect place for your", list_plants[2])
            score -= 5
            techniques.show_score(score)
            return score

    elif type != "yes" or type == "":
        print("No selection made.")
        Summer_squash_season(score)
        return score


def Pepper_season(score):
    weather_sltd = random.choice(best_season)
    season(list_plants[3], best_season[1])
    type = input("Type YES, to make a random selection.")
    if type == "yes":
        print("The season choice you made is:", weather_sltd)

        if weather_sltd == "Spring":
            print("Congratulation,your",
                  list_plants[3], "is happy and waves at you from this", weather_sltd)
            x = 5
            score = score + x
            techniques.show_score(score)
            return score

        elif weather_sltd != "Spring":
            print("This is not the perfect place for your", list_plants[3])
            score -= 5
            techniques.show_score(score)
            return score

    elif type != "yes" or type == "":
        print("No selection made.")
        Pepper_season(score)
        return score


def Strawberries_season(score):
    weather_sltd = random.choice(best_season)
    season(list_plants[4], best_season[1])
    type = input("Type YES, to make a random selection.")
    if type == "yes":
        print("The season choice you made is:", weather_sltd)

        if weather_sltd == "Spring":
            print("Congratulation,your",
                  list_plants[4], "is happy and waves at you from this", weather_sltd)
            x = 5
            score = score + x
            techniques.show_score(score)
            return score

        elif weather_sltd != "Spring":
            print("This is not the perfect place for your", list_plants[4])
            score -= 5
            techniques.show_score(score)
            return score

    elif type != "yes" or type == "":
        print("No selection made.")
        Strawberries_season(score)
        return score


def Thyme_season(score):
    weather_sltd = random.choice(best_season)
    season(list_plants[5], best_season[1])
    type = input("Type YES, to make a random selection.")
    if type == "yes":
        print("The season choice you made is:", weather_sltd)

        if weather_sltd == "Spring":
            print("Congratulation,your",
                  list_plants[5], "is happy and waves at you from this", weather_sltd)
            x = 5
            score = score + x
            techniques.show_score(score)
            return score

        elif weather_sltd != "Spring":
            print("This is not the perfect place for your", list_plants[5])
            score -= 5
            techniques.show_score(score)
            return score

    elif type != "yes" or type == "":
        print("No selection made.")
        Thyme_season(score)
        return score


def Cucumber_season(score):
    weather_sltd = random.choice(best_season)
    season(list_plants[6], best_season[0])
    type = input("Type YES, to make a random selection.")
    if type == "yes":
        print("The season choice you made is:", weather_sltd)

        if weather_sltd == "Summer":
            print("Congratulation,your",
                  list_plants[6], "is happy and waves at you from this", weather_sltd)
            x = 5
            score = score + x
            techniques.show_score(score)
            return score

        elif weather_sltd != "Summer":
            print("This is not the perfect place for your", list_plants[6])
            score -= 5
            techniques.show_score(score)
            return score

    elif type != "yes" or type == "":
        print("No selection made.")
        Cucumber_season(score)
        return score
