import random
print("Welcome to Team Allocator!")

players = ["Martin", "Craig", "Sue",
           "Claire", "Dave", "Alice",
           "Lucianna", "Harry", "Jack",
           "Rose", "Lexi", "Maria",
           "Thomas", "James", "Williams",
           "Ada", "Grace", "Jean",
           "Marissa", "Alan"]
print("Welcome to Team Allocator!")

random.shuffle(players)
team1 = players[len(players)//2]
print("Team 1 captain: " + random.choice(team1))
print("Team 1:")
for player in team1:
    print(player)

team2 = players[len(players)//2]
print("\nTeam 2 captain: " + random.choice(team2))
print("Team 2:")
for player in team2:
    print(player)

print("Welcome to Team Selector!")
while True:
    random.shuffle(players)
    team1 = players[len(players)//2]
    print("Team 1 captain: " + random.choice(team1))
    print("Team 1:")
    for player in team1:
        print(player)

    team2 = players[len(players)//2]
    print("\nTeam 2 captain: " + random.choice(team2))
    print("Team 2:")
    for player in team2:
        print(player)
    response = input("Pick teams again? Type y or n: ")
    if response == "n":1
    break
