import pickle
import time


Highscores = []
Top_10 = []

# Get today in DD/MM/YYYY
def date():
    current_year = time.localtime().tm_year
    current_month = time.localtime().tm_mon
    current_day = time.localtime().tm_mday
    return_string = str(current_day) + " / " + str(current_month) + " / " + str(current_year)
    return return_string

# When a 11th score is added  -> delete the lowest one
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

# Add new highscore
def new_highscore(name, highscore, date):
    locallist = []
    locallist.append(name)
    locallist.append(highscore)
    locallist.append(date)
    Highscores.append(locallist)
    Top_10.append(locallist)
    return remove_lowest_score()

# load top 10 highscores from file
def load_highscores():
    with open("highscore.txt", "rb") as highscorefile:
        Top_10 = pickle.load(highscorefile)
    return Top_10

# write top 10 highscores to file
def write_highscores(Top_10):
    with open("highscore.txt", "wb") as highscorefile:
        Top_10 = pickle.dump(Top_10, highscorefile)

# Test data
user_name = "Pika"
user_score = 8700
user_date = date()

new_highscore(user_name, user_score, user_date)
print(Top_10)
new_highscore("Example Person", 8600, date())
print(Top_10)
new_highscore("Example Person 2", 8500, date())
print(Top_10)

write_highscores(Top_10)






