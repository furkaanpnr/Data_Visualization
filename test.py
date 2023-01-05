import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_json('tets.json') # load data from json file to dict

game1Info = data["games"]["game1"]
game2Info = data["games"]["game2"]
game3Info = data["games"]["game3"]

game1Score = game1Info["scores"]
score1 = list(game1Score.values())
game2Score = game2Info["scores"]
score2 = list(game2Score.values())
game3Score = game3Info["scores"]
score3 = list(game3Score.values())

# gets the scores for each game
redScores = [data["games"]["game"+str(i+1)]["scores"]["red"] for i in range(len(data))]
blueScores = [data["games"]["game"+str(i+1)]["scores"]["blue"] for i in range(len(data))]
greenScores = [data["games"]["game"+str(i+1)]["scores"]["green"] for i in range(len(data))]
whiteScores = [data["games"]["game"+str(i+1)]["scores"]["white"] for i in range(len(data))]

###compare for all games and all players
#plt.plot(redScores, label="red", color="red", marker="o", linestyle="dashed")
#plt.plot(blueScores, label="blue", color="blue", marker="o", linestyle="dashed")
#plt.plot(greenScores, label="green", color="green", marker="o", linestyle="dashed")
#plt.plot(whiteScores, label="white", color="black", marker="o", linestyle="dashed")
#plt.legend()
#plt.grid()
#plt.title("Scores for all games")
#plt.show()

###compare game1 scores for all players
#x = np.array(["RED", "BLUE", "GREEN", "WHITE"])
#y = np.array(score1)
#plt.xlabel("AI Players")
#plt.ylabel("Scores")
#plt.title("Game1 Results")
#plt.bar(x, y)
#plt.show()

### compare game1 scores with pie chart
#y = np.array(score1)
#plt.title("Game1 Results")
#labels = ["RED", "BLUE", "GREEN", "WHITE"]
#colors = ["red","blue","green","cyan"]
#explode = (0, 0, 0.2, 0)# only "explode" the 3rd slice
#plt.pie(y, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, explode=explode)
#plt.legend(title="AI Players", loc="best", bbox_to_anchor=(0.8, 0.1, 0.5, 1))
#plt.show()

### compare RED AI's scores in all games with scatter graph
#x = [game+1 for game in range(len(data))]
#y = redScores
#plt.xlabel("Games")
#plt.ylabel("RED AI's scores")
#plt.scatter(x,y)
#plt.show()

### compare all AI scores
#>> RED AI 
x = [game+1 for game in range(len(data))]
y = redScores
plt.scatter(x, y, color="red")

#>> BLUE AI
x = [game+1 for game in range(len(data))]
y = blueScores
plt.scatter(x, y, color="blue")

#>> GREEN AI
x = [game+1 for game in range(len(data))]
y = greenScores
plt.scatter(x, y, color="green")

#>> WHITE AI
x = [game+1 for game in range(len(data))]
y = whiteScores
plt.scatter(x, y, color="cyan")

plt.xlabel("GAMES")
plt.ylabel("AI's SCORES")
plt.title("RESULT OF ENTİRE GAME")
#plt.colorbar()
plt.show()