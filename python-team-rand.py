import random

print("Build your own random sport team!")

first_names = [
    # Male Names
    "Liam", "Noah", "Oliver", "Ethan", "Aiden", "Mason", "Caden", "Jackson", "Lucas", "Logan",
    "Elijah", "Michael", "Alexander", "James", "William", "Benjamin", "Daniel", "Henry", "Joseph", "Matthew",

    # Female Names
    "Olivia", "Emma", "Ava", "Sophia", "Isabella", "Mia", "Amelia", "Harper", "Evelyn", "Abigail",
    "Emily", "Elizabeth", "Sofia", "Ella", "Scarlett", "Grace", "Chloe", "Victoria", "Zoe", "Hannah"
]

print("Time to randomize the 2 teams....")
random.shuffle(first_names)
