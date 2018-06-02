import pickle
import time


def date():
    current_year = time.localtime().tm_year
    current_month = time.localtime().tm_mon
    current_day = time.localtime().tm_mday
    return_string = str(current_day) + " / " + str(current_month) + " / " + str(current_year)
    return return_string


Highscores = []

Top_10 = []


def remove_lowest_score():
    if len(Highscores) > 10:
        scores = []
        for i in Highscores:
            scores.append(i[1])
        score_index = scores.index(min(scores))
        Top_10.remove(Highscores[score_index])
        return Top_10
    else:
        return Highscores


def new_highscore(name, highscore, date):
    locallist = []
    locallist.append(name)
    locallist.append(highscore)
    locallist.append(date)
    Highscores.append(locallist)
    Top_10.append(locallist)
    return remove_lowest_score()


user_name = "Pika"
user_score = 8700
user_date = date()

new_highscore(user_name, user_score, user_date)
print(Top_10)
new_highscore("User1", 8600, date())
print(Top_10)
new_highscore("User2", 8500, date())
print(Top_10)
new_highscore("User3", 8500, date())
print(Top_10)
new_highscore("User4", 8500, date())
print(Top_10)
new_highscore("User5", 8500, date())
print(Top_10)
new_highscore("User6", 8500, date())
print(Top_10)
new_highscore("User7", 8500, date())
print(Top_10)
new_highscore("User8", 8500, date())
print(Top_10)
new_highscore("User9", 8500, date())
print(Top_10)
new_highscore("User10", 8500, date())
print(Top_10)
new_highscore("User11", 8500, date())
print(Top_10)


def load_highscores():
    with open("highscore.txt", "rb") as highscorefile:
        Top_10 = pickle.load(highscorefile)
    return Top_10


def write_highscores(Top_10):
    with open("highscore.txt", "wb") as highscorefile:
        Top_10 = pickle.dump(Top_10, highscorefile)


write_highscores(Top_10)