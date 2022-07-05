from my_project_pkg import techniques, techniques_seasons, techniques_where_to_plant, techniques_harvest_time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

score = float(0)


def plants():

    print("----------------------------------------")
    print(Fore.GREEN + "|    Lettuce     |    Tomatoes         |")
    print("----------------------------------------")
    print(Fore.YELLOW + "|    Beans       |     Scallions       |")
    print("----------------------------------------")
    print(Fore.GREEN + "|    Eggplant    |     Summer squash   |")
    print("----------------------------------------")
    print(Fore.RED + "|    Pepper      |     Strawberries    |")
    print("----------------------------------------")
    print(Fore.GREEN + "|    Thymes      |     Cucumbers       |")
    print("----------------------------------------")
    print(Fore.RED + "|             Exit Game                |")
    print("----------------------------------------")


def inst():
    print("------------------------------------------------------------------------------------")
    print("|    1)Prefered weather for max growth     |    2)Best season for planting         |")
    print("------------------------------------------------------------------------------------")
    print("|    3) Where to plant                       |     4) Harvest time                 |")
    print("------------------------------------------------------------------------------------")
    print("|                                      5) Go Back                                  |")
    print("------------------------------------------------------------------------------------")


print(Fore.GREEN + Back.WHITE + Style.DIM +
      "Welcome to your HERTICULTURE GAME.")
print(Fore.GREEN + Back.WHITE + Style.DIM + "Here we train while playing")
print(Fore.GREEN + Back.WHITE + Style.DIM +
      "making this game best for fun and technics")
print(Fore.GREEN + Back.WHITE + Style.DIM + "aquisition in gardening !")

while True:
    plants()
    choice = input(
        "Make a choice of plants to start game or type EXIT to leave game:")

    if choice == "Lettuce":
        print("You Choosed:", Fore.GREEN + choice)
        while True:
            inst()
            lett = input(
                "choose one of the options to play any of the different sections: ")
            if lett == "1":
                score = techniques.Lettuce(score)

            elif lett == "2":
                score = techniques_seasons.Lettuce_season(score)

            elif lett == "3":
                score = techniques_where_to_plant.Lettuce_place(score)

            elif lett == "4":
                score = techniques_harvest_time.Lettuce_harvest(score)

            elif lett == "5":
                break

    elif choice == "Tomatoes":
        print("You Choosed:", Fore.RED + choice)
        while True:
            inst()
            lett = input(
                "choose one of the options to play any of the sections: ")
            if lett == "1":
                score = techniques.Tomatoes(score)

            elif lett == "2":
                score = techniques_seasons.Tomatoes_season(score)

            elif lett == "3":
                score = techniques_where_to_plant.Tomatoes_place(score)

            elif lett == "4":
                score = techniques_harvest_time.Tomatoes_harvest(score)

            elif lett == "5":
                break

    elif choice == "Beans":
        print("You Choosed:", Fore.YELLOW + choice)
        while True:
            inst()
            lett = input(
                "choose one of the options to play any of the different sections: ")
            if lett == "1":
                score = techniques.Beans(score)

            elif lett == "2":
                score = techniques_seasons.Beans_season(score)

            elif lett == "3":
                score = techniques_where_to_plant.Beans_place(score)

            elif lett == "4":
                score = techniques_harvest_time.Beans_harvest(score)

            elif lett == "5":
                break

    elif choice == "Scallions":
        print("You Choosed:", Fore.GREEN + choice)
        while True:
            inst()
            lett = input(
                "choose one of the options to play any of the different sections. ")
            if lett == "1":
                score = techniques.Scallions(score)

            elif lett == "2":
                score = techniques_seasons.Scallions_season(score)

            elif lett == "3":
                score = techniques_where_to_plant.Scallions_place(score)

            elif lett == "4":
                score = techniques_harvest_time.Scallion_harvest(score)

            elif lett == "5":
                break

    elif choice == "Eggplant":
        print("You Choosed:", Fore.GREEN + choice)
        while True:
            inst()
            lett = input(
                "choose one of the options to play any of the different sections. ")
            if lett == "1":
                score = techniques.Eggplant(score)

            elif lett == "2":
                score = techniques_seasons.Eggplant_season(score)

            elif lett == "3":
                score = techniques_where_to_plant.Eggplant_place(score)

            elif lett == "4":
                score = techniques_harvest_time.Eggplant_harvest(score)

            elif lett == "5":
                break

    elif choice == "Summer squash":
        print("You Choosed:", Fore.GREEN + choice)
        while True:
            inst()
            lett = input(
                "choose one of the options to play any of the different sections. ")
            if lett == "1":
                score = techniques.Summer_squash(score)

            elif lett == "2":
                score = techniques_seasons.Summer_squash_season(score)

            elif lett == "3":
                score = techniques_where_to_plant.Summer_squash_place(score)

            elif lett == "4":
                score = techniques_harvest_time.Summer_squash_harvest(score)

            elif lett == "5":
                break

    elif choice == "Pepper":
        print("You Choosed:", Fore.RED + choice)
        while True:
            inst()
            lett = input(
                "choose one of the options to play any of the different sections. ")
            if lett == "1":
                score = techniques.Pepper(score)

            elif lett == "2":
                score = techniques_seasons.Pepper_season(score)

            elif lett == "3":
                score = techniques_where_to_plant.Pepper_place(score)

            elif lett == "4":
                score = techniques_harvest_time.Pepper_harvest(score)

            elif lett == "5":
                break

    elif choice == "Strawberries":
        print("You Choosed:", Fore.RED + choice)
        while True:
            inst()
            lett = input(
                "choose one of the options to play any of the different sections. ")
            if lett == "1":
                score = techniques.Strawberries(score)

            elif lett == "2":
                score = techniques_seasons.Strawberries_season(score)

            elif lett == "3":
                score = techniques_where_to_plant.Strawberries_place(score)

            elif lett == "4":
                score = techniques_harvest_time.Strawberries_harvest(score)

            elif lett == "5":
                break

    elif choice == "Thymes":
        print("You Choosed:", Fore.GREEN + choice)
        while True:
            inst()
            lett = input(
                "choose one of the options to play any of the different sections. ")
            if lett == "1":
                score = techniques.Thymes(score)

            elif lett == "2":
                score = techniques_seasons.Thyme_season(score)

            elif lett == "3":
                score = techniques_where_to_plant.Thyme_place(score)

            elif lett == "4":
                score = techniques_harvest_time.Thyme_harvest(score)

            elif lett == "5":
                break

    elif choice == "Cucumbers":
        print("You Choosed:", Fore.GREEN + choice)
        while True:
            inst()
            lett = input(
                "choose one of the options to play any of the different sections. ")
            if lett == "1":
                score = techniques.Cucumbers(score)

            elif lett == "2":
                score = techniques_seasons.Cucumber_season(score)

            elif lett == "3":
                score = techniques_where_to_plant.Cucumber_place(score)

            elif lett == "4":
                score = techniques_harvest_time.Cucumber_harvest(score)

            elif lett == "5":
                break

    elif choice == "EXIT":
        techniques.ext_game(score)
        break
