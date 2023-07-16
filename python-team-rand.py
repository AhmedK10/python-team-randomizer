import random

print("Build your own random sport team!")

names = [
    # Male Names
    "Liam", "Noah", "Oliver", "Ethan", "Aiden", "Mason", "Caden", "Jackson", "Lucas", "Logan",
    "Elijah", "Michael", "Alexander", "James", "William", "Benjamin", "Daniel", "Henry", "Joseph", "Matthew",

    # Female Names
    "Olivia", "Emma", "Ava", "Sophia", "Isabella", "Mia", "Amelia", "Harper", "Evelyn", "Abigail",
    "Emily", "Elizabeth", "Sofia", "Ella", "Scarlett", "Grace", "Chloe", "Victoria", "Zoe", "Hannah"
]

print("Time to randomize the teams....")
random.shuffle(names)

#spliting the randomized list to 2 teams.....starting with team1
first_team = names[:len(names)//2]
print("")

#picking a captain randomly for the team
team1_cap = random.choice(first_team)
print("Team 1's Captain is:", team1_cap)

#dispalying the first team:
print("")
print("Team 1:")
for member in first_team:
    print(member)
print("")
