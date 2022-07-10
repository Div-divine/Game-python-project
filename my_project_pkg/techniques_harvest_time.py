from msilib.schema import Font
from my_project_pkg import techniques
import random
from colorama import Fore, Back, Style


list_plants = [Fore.GREEN + "Scallions", Fore.GREEN + "Eggplants", Fore.GREEN + "Summer squash", Fore.RED + "Pepper",
               Fore.RED + "Strawberies", Fore.GREEN + "Thymes", Fore.GREEN + "Cucumbers", Fore.GREEN + "Lettuce", Fore.RED + "Tomatoes", Fore.GREEN + "Beans"]


def harvest_choice(list_plants, weather_sltd):

    print(Fore.YELLOW + "You want to harvest your", list_plants, Fore.YELLOW +
          "after", weather_sltd, Fore.YELLOW + "days")


def harvest_message(x, y, list_plants):
    print(Fore.RED + "The best time for havasting", Fore.RED + list_plants,
          Fore.RED + "is within", Fore.RED + x, Fore.RED + "to", Fore.RED + y, Fore.RED + "days")


def Lettuce_harvest(score):
    weather_sltd = random.randint(20, 75)
    type = input("Type YES, to make a random selection.")
    if type == "YES":
        harvest_message("30", "60", list_plants[7])
        harvest_choice(
            Fore.GREEN + list_plants[7], Fore.GREEN + str(weather_sltd))

        if weather_sltd >= 30 and weather_sltd <= 60:

            print(Fore.GREEN + "Congratulation,your", Fore.GREEN +
                  list_plants[7], Fore.GREEN + "is ready!")
            x = 5
            score = score + x
            techniques.show_score(score)
            return score

        elif weather_sltd < 30:
            print(Fore.CYAN + "Your", Fore.CYAN +
                  list_plants[7], Fore.CYAN + "is too young!")
            score -= 5
            techniques.show_score(score)
            return score

        elif weather_sltd > 60:
            print(Fore.RED + "Your", Fore.GREEN +
                  list_plants[7], Fore.RED + "is too old!")
            score -= 5
            techniques.show_score(score)
            return score

    elif type != "YES" or type == "":
        print(Fore.RED + "No selection made.")
        Lettuce_harvest(score)
        return score


def Tomatoes_harvest(score):
    weather_sltd = random.randint(50, 120)
    type = input("Type YES, to make a random selection.")
    if type == "YES":
        harvest_message("60", "100", list_plants[8])
        harvest_choice(
            Fore.RED + list_plants[8], Fore.RED + str(weather_sltd))

        if weather_sltd >= 60 and weather_sltd <= 100:

            print(Fore.GREEN + "Congratulation,your", Fore.RED +
                  list_plants[8], Fore.GREEN + "is ready!")
            x = 5
            score = score + x
            techniques.show_score(score)
            return score

        elif weather_sltd < 60:
            print(Fore.CYAN + "Your", Fore.CYAN +
                  list_plants[8], Fore.CYAN + "is too young!")
            score -= 5
            techniques.show_score(score)
            return score

        elif weather_sltd > 120:
            print(Fore.RED + "Your", Fore.YELLOW +
                  list_plants[8], Fore.YELLOW + "is too old!")
            score -= 5
            techniques.show_score(score)
            return score

    elif type != "YES" or type == "":
        print(Fore.RED + "No selection made.")
        Tomatoes_harvest(score)
        return score


def Beans_harvest(score):
    weather_sltd = random.randint(50, 70)
    type = input("Type YES, to make a random selection.")
    if type == "YES":
        harvest_message(
            "65", "more,but don't wait to long, if you need it fresh", list_plants[9])
        harvest_choice(
            Fore.GREEN + list_plants[9], Fore.GREEN + str(weather_sltd))

        if weather_sltd >= 65:

            print(Fore.GREEN + "Congratulation,your", Fore.GREEN +
                  list_plants[9], Fore.GREEN + "is ready!")
            x = 5
            score = score + x
            techniques.show_score(score)
            return score

        else:
            print(Fore.RED + "Your", Fore.GREEN +
                  list_plants[9], Fore.YELLOW + "is too young!")
            score -= 5
            techniques.show_score(score)
            return score

    elif type != "YES" or type == "":
        print(Fore.RED + "No selection made.")
        Beans_harvest(score)
        return score


def Scallion_harvest(score):
    weather_sltd = random.randint(50, 85)
    type = input("Type YES, to make a random selection.")
    if type == "YES":
        harvest_message("60", "80", list_plants[0])
        harvest_choice(
            Fore.GREEN + list_plants[0], Fore.GREEN + str(weather_sltd))

        if weather_sltd >= 60 and weather_sltd <= 80:

            print(Fore.GREEN + "Congratulation,your", Fore.GREEN +
                  list_plants[0], Fore.GREEN + "is ready!")
            x = 5
            score = score + x
            techniques.show_score(score)
            return score

        elif weather_sltd < 60:
            print(Fore.CYAN + "Your", Fore.CYAN +
                  list_plants[0], Fore.CYAN + "is too young!")
            score -= 5
            techniques.show_score(score)
            return score

        elif weather_sltd > 80:
            print(Fore.YELLOW + "Your", Fore.YELLOW +
                  list_plants[0], Fore.YELLOW + "is too old!")
            score -= 5
            techniques.show_score(score)
            return score

    elif type != "YES" or type == "":
        print(Fore.RED + "No selection made.")
        Scallion_harvest(score)
        return score


def Eggplant_harvest(score):
    weather_sltd = random.randint(80, 150)
    type = input("Type YES, to make a random selection.")
    if type == "YES":
        harvest_message("100", "120", list_plants[1])
        harvest_choice(
            Fore.GREEN + list_plants[1], Fore.GREEN + str(weather_sltd))

        if weather_sltd >= 100 and weather_sltd <= 120:

            print(Fore.GREEN + "Congratulation,your", Fore.GREEN +
                  list_plants[1], Fore.GREEN + "is ready!")
            x = 5
            score = score + x
            techniques.show_score(score)
            return score

        elif weather_sltd < 100:
            print(Fore.CYAN + "Your", Fore.GREEN +
                  list_plants[1], Fore.CYAN + "is too young!")
            score -= 5
            techniques.show_score(score)
            return score

        elif weather_sltd > 120:
            print(Fore.YELLOW + "Your", Fore.YELLOW +
                  list_plants[1], Fore.YELLOW + "is too old!")
            score -= 5
            techniques.show_score(score)
            return score

    elif type != "YES" or type == "":
        print(Fore.RED + "No selection made.")
        Eggplant_harvest(score)
        return score


def Summer_squash_harvest(score):
    weather_sltd = random.randint(50, 65)
    type = input("Type YES, to make a random selection.")
    if type == "YES":
        harvest_message(
            "60", "more,but don't wait to long, if you need it fresh", list_plants[2])
        harvest_choice(
            Fore.GREEN + list_plants[2], Fore.GREEN + str(weather_sltd))

        if weather_sltd >= 60:

            print(Fore.GREEN + "Congratulation,your", Fore.GREEN +
                  list_plants[2], Fore.GREEN + "is ready!")
            x = 5
            score = score + x
            techniques.show_score(score)
            return score

        else:
            print(Fore.RED + "Your", Fore.GREEN +
                  list_plants[2], Fore.YELLOW + "is too young!")
            score -= 5
            techniques.show_score(score)
            return score

    elif type != "YES" or type == "":
        print(Fore.RED + "No selection made.")
        Summer_squash_harvest(score)
        return score


def Pepper_harvest(score):
    weather_sltd = random.randint(50, 120)
    type = input("Type YES, to make a random selection.")
    if type == "YES":
        harvest_message("60", "90", list_plants[3])
        harvest_choice(
            Fore.RED + list_plants[3], Fore.RED + str(weather_sltd))

        if weather_sltd >= 60 and weather_sltd <= 90:

            print(Fore.GREEN + "Congratulation,your", Fore.RED +
                  list_plants[3], Fore.GREEN + "is ready!")
            x = 5
            score = score + x
            techniques.show_score(score)
            return score

        elif weather_sltd < 60:
            print(Fore.GREEN + "Your", Fore.GREEN +
                  list_plants[3], Fore.GREEN + "is too young!")
            score -= 5
            techniques.show_score(score)
            return score

        elif weather_sltd > 90:
            print(Fore.YELLOW + "Your", Fore.YELLOW +
                  list_plants[3], Fore.YELLOW + "is too old!")
            score -= 5
            techniques.show_score(score)
            return score

    elif type != "YES" or type == "":
        print(Fore.RED + "No selection made.")
        Pepper_harvest(score)
        return score


def Strawberries_harvest(score):

    weather_sltd = random.randint(105, 160)
    type = input("Type YES, to make a random selection.")
    if type == "YES":
        harvest_message("120", "140", list_plants[4])
        harvest_choice(
            Fore.RED + list_plants[4], Fore.RED + str(weather_sltd))

        if weather_sltd >= 120 and weather_sltd <= 140:

            print(Fore.RED + "Congratulation,your", Fore.RED +
                  list_plants[4], Fore.RED + "is ready!")
            x = 5
            score = score + x
            techniques.show_score(score)
            return score

        elif weather_sltd < 120:
            print(Fore.CYAN + "Your", Fore.GREEN +
                  list_plants[4], Fore.CYAN + "is too young!")
            score -= 5
            techniques.show_score(score)
            return score

        elif weather_sltd > 140:
            print(Fore.YELLOW + "Your", Fore.YELLOW +
                  list_plants[4], Fore.YELLOW + "is too old!")
            score -= 5
            techniques.show_score(score)
            return score

    elif type != "YES" or type == "":
        print(Fore.RED + "No selection made.")
        Strawberries_harvest(score)
        return score


def Thyme_harvest(score):
    weather_sltd = random.randint(20, 35)
    type = input("Type YES, to make a random selection.")
    if type == "YES":
        harvest_message(
            "28", "more,but don't wait to long, if you need it fresh", list_plants[5])
        harvest_choice(
            Fore.GREEN + list_plants[5], Fore.GREEN + str(weather_sltd))

        if weather_sltd >= 28:

            print(Fore.GREEN + "Congratulation,your", Fore.GREEN +
                  list_plants[5], Fore.GREEN + "is ready!")
            x = 5
            score = score + x
            techniques.show_score(score)
            return score

        else:
            print(Fore.RED + "Your", Fore.GREEN +
                  list_plants[5], Fore.GREEN + "is too young!")
            score -= 5
            techniques.show_score(score)
            return score

    elif type != "YES" or type == "":
        print(Fore.RED + "No selection made.")
        Thyme_harvest(score)
        return score


def Cucumber_harvest(score):
    weather_sltd = random.randint(40, 85)
    type = input("Type YES, to make a random selection.")
    if type == "YES":
        harvest_message("50", "70", list_plants[6])
        harvest_choice(
            Fore.GREEN + list_plants[6], Fore.GREEN + str(weather_sltd))

        if weather_sltd >= 50 and weather_sltd <= 70:

            print(Fore.GREEN + "Congratulation,your", Fore.GREEN +
                  list_plants[6], Fore.GREEN + "is ready!")
            x = 5
            score = score + x
            techniques.show_score(score)
            return score

        elif weather_sltd < 50:
            print(Fore.CYAN + "Your", Fore.GREEN +
                  list_plants[6], Fore.GREEN + "is too young!")
            score -= 5
            techniques.show_score(score)
            return score

        elif weather_sltd > 70:
            print(Fore.YELLOW + "Your", Fore.YELLOW +
                  list_plants[6], Fore.YELLOW + "is too old!")
            score -= 5
            techniques.show_score(score)
            return score

    elif type != "YES" or type == "":
        print(Fore.RED + "No selection made.")
        Cucumber_harvest(score)
        return score
