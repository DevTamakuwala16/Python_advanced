player_name = input("Enter you hero's name: ")
score = int(input("Enter your score: "))

with open ("Dev_score.txt", "w") as file
    file.write(f"Player: {player_name}/n")
    file.write(f"Score: {score}/n")
    
print("Your score has been saved")

try:
    with open("Dev_score.txt", "r") as file
    print("Memory Crystal Reveals: ")
    print(file.read())
except FileNotFoundError
    print("No previous score found.")

try:
    with open("Dev_score.txt", "r") as file
    file.readline()
    old_score = int(file.readline().split(":")[1])
except FileNotFoundError:
    old_score = 0

earned = int(input("Points earned this round: "))
new_score = old_score + earned

with open("Dev_score.txt", "w") as file
    file.write(f"Player: {player_name}/n")
    file.write(f"Score: {new_score}/n")
    
print(f"Score updated to {new_score}")
    
current_score = int(input("Enter your score: "))

try:
    with open("Dev_score.txt", "r") as file
        high_score = int(file.read())
    except FileNotFoundError:
        high_score = 0
        
if current_score > high_score:
    with open("Dev_score.txt", "w") as file
        file.write(str(current_score))
    print("New High Score")
else:
    print(f"High Score to Beat: {high_score}")
    
player = input("Hero name: ")
score = int(input("Score: "))

scores = {}

try:
    with open("Dev_score.txt", "r") as file
    for line in file:
        name, pts = line.strip().split(":")
        scores[name] = int(pts)
    except FileNotFoundError:
        pass
    
    scores[player] = score
    
    with open("Dev_score.txt", "w") as file
    for name, pts in scores.items():

      