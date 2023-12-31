import random

print("Build your own random sport teams!")

while True:
    print("")
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

    #asking the user is it a team or individual sport
    response = input("Is this an individual or team sport? (type: individual or team)\n")

    if response == "team":

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

        #TEAM 2:
        second_team = names[len(names)//2:]
        print("")

        #picking a captain randomly for the team
        team2_cap = random.choice(second_team)
        print("Team 2's Captain is:", team2_cap)

        #dispalying the first team:
        print("")
        print("Team 2:")
        for member in second_team:
            print(member)
        print("")

    else:
        print("")
        for i in range (0, 40, 2):
            print(names[i] + " will play against " + names[i+1])
            starting_player = random.randrange(i, i+2)
            print(names[starting_player] + " will start the match")

    #asking the user if they are happy with the teams
    print("")
    answer = input("Pick teams again or are you happy with them? Type 'yes' or 'no' below:\n")
    if answer == "no":
        break
