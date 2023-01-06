import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_json('results.json')# load data

# constants
labels = ["WHITE", "RED", "GREEN", "BLUE"]
colors = ["cyan",'#FF2E2E','#2AFF22','#2660FF']

### Game 1 Results
#game1Info = data["games"]["game1"]["scores"]
#game1Score = list(game1Info.values())
## Game 1 Results with pie chart
#y = np.array(game1Score)
#explode = (0, 0, 0, 0.1)
#plt.title("Game 1 Results")
#plt.pie(y, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, explode=explode)
#plt.legend(title="AI Players", loc="best", bbox_to_anchor=(0.8, 0.1, 0.5, 1))
#plt.show()


### Game 2 Results
#game2Info = data["games"]["game2"]["scores"]
#game2Score = list(game2Info.values())
#
## Game 2 Results with pie chart
#y = np.array(game2Score)
#explode = (0, 0, 0, 0.1)
#plt.title("Game 2 Results")
#plt.pie(y, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, explode=explode)
#plt.legend(title="AI Players", loc="best", bbox_to_anchor=(0.8, 0.1, 0.5, 1))
#plt.show()

### Game 3 Results
#game3Info = data["games"]["game3"]["scores"]
#game3Score = list(game3Info.values())
#
## Game 3 Results with pie chart
#y = np.array(game3Score)
#explode = (0, 0, 0.1, 0.1)
#plt.title("Game 3 Results")
#plt.pie(y, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, explode=explode)
#plt.legend(title="AI Players", loc="best", bbox_to_anchor=(0.8, 0.1, 0.5, 1))
#plt.show()


### Game 4 Results
#game4Info = data["games"]["game4"]["scores"]
#game4Score = list(game4Info.values())
#
## Game 4 Results with pie chart
#y = np.array(game4Score)
#explode = (0, 0, 0.1, 0)
#plt.title("Game 4 Results")
#plt.pie(y, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, explode=explode)
#plt.legend(title="AI Players", loc="best", bbox_to_anchor=(0.8, 0.1, 0.5, 1))
#plt.show()


### Game 5 Results
#game5Info = data["games"]["game5"]["scores"]
#game5Score = list(game5Info.values())
#
## Game 5 Results with pie chart
#y = np.array(game5Score)
#explode = (0, 0.1, 0, 0)
#plt.title("Game 5 Results")
#plt.pie(y, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, explode=explode)
#plt.legend(title="AI Players", loc="best", bbox_to_anchor=(0.8, 0.1, 0.5, 1))
#plt.show()


### Game 6 Results
#game6Info = data["games"]["game6"]["scores"]
#game6Score = list(game6Info.values())
#
## Game 6 Results with pie chart
#y = np.array(game6Score)
#explode = (0.1, 0, 0, 0)
#plt.title("Game 6 Results")
#plt.pie(y, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, explode=explode)
#plt.legend(title="AI Players", loc="best", bbox_to_anchor=(0.8, 0.1, 0.5, 1))
#plt.show()


### All Game Results
whiteScores = [data["games"]["game"+ str(i+1)]["scores"]["white"] for i in range(len(data))]
redScores = [data["games"]["game"+ str(i+1)]["scores"]["red"] for i in range(len(data))]
greenScores = [data["games"]["game"+ str(i+1)]["scores"]["green"] for i in range(len(data))]
blueScores = [data["games"]["game"+ str(i+1)]["scores"]["blue"] for i in range(len(data))]

default_x_ticks = range(len(data)) # game number

#plt.plot(whiteScores, label="white", color="cyan", marker="o", linestyle="dashed")
#plt.plot(redScores, label="red", color="red", marker="o", linestyle="dashed")
#plt.plot(greenScores, label="green", color="green", marker="o", linestyle="dashed")
#plt.plot(blueScores, label="blue", color="blue", marker="o", linestyle="dashed")
#
#plt.grid(linewidth=0.5, linestyle="--")
#plt.xticks(default_x_ticks, [game+1 for game in range(len(data))])
#plt.legend(title="AI Players", loc="best", bbox_to_anchor=(0.6, 0.1, 0.5, 1))
#
#plt.ylabel("Score")
#plt.xlabel("Game Number")
#plt.title("All Game Results")
#plt.show()

#> only white
#plt.plot(whiteScores, label="white", color="cyan", marker="o", linestyle="dashed")
#plt.grid(linewidth=0.5, linestyle="--")
#plt.xticks(default_x_ticks, [game+1 for game in range(len(data))])
#plt.legend(title="AI Players", loc="best", bbox_to_anchor=(0.6, 0.15, 0.5, 1))
#
#plt.ylabel("Score")
#plt.xlabel("Game Number")
#plt.title("All Game Results")
#plt.show()

#> only red
#plt.plot(redScores, label="red", color="red", marker="o", linestyle="dashed")
#plt.grid(linewidth=0.5, linestyle="--")
#plt.xticks(default_x_ticks, [game+1 for game in range(len(data))])
#plt.legend(title="AI Players", loc="best", bbox_to_anchor=(0.6, 0.15, 0.5, 1))
#
#plt.ylabel("Score")
#plt.xlabel("Game Number")
#plt.title("All Game Results")
#plt.show()

#> only green
#plt.plot(greenScores, label="green", color="green", marker="o", linestyle="dashed")
#plt.grid(linewidth=0.5, linestyle="--")
#plt.xticks(default_x_ticks, [game+1 for game in range(len(data))])
#plt.legend(title="AI Players", loc="best", bbox_to_anchor=(0.6, 0.15, 0.5, 1))
#
#plt.ylabel("Score")
#plt.xlabel("Game Number")
#plt.title("All Game Results")
#plt.show()

#> only blue
plt.plot(blueScores, label="blue", color="blue", marker="o", linestyle="dashed")
plt.grid(linewidth=0.5, linestyle="--")
plt.xticks(default_x_ticks, [game+1 for game in range(len(data))])
plt.legend(title="AI Players", loc="best", bbox_to_anchor=(0.6, 0.15, 0.5, 1))

plt.ylabel("Score")
plt.xlabel("Game Number")
plt.title("All Game Results")
plt.show()