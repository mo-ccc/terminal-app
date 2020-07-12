import user
import fetch

current_map = "map.txt"

while True:
    entry = input("input: ")
    if entry == "quit":
        print("goodbye")
        break
    user.userinput(entry, current_map)
    if current_map == "map.txt":
        if user.cave_entered == True:
            current_map = "cave.txt"
    elif current_map == "cave.txt":
        if user.cave_exited == True:
            current_map = "map.txt"
    else:
        current_map = "map.txt"

    
