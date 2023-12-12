print("Water and Defense Game!")
player = input( "Enter your name:  ")
player_age = input("Enter your age: ")

if int(player_age) >= 18:
    print(f"Player {player.title()} is eligible to play water and defense game!")
    print("Welcome to Water and Defense Game!")
    defense = 10
    print(f"You are starting with {defense} defense points.")
    
    wants_to_play = input("Do you want to play?  ").lower()
    if wants_to_play == "yes":
        print("Let's play!") 
        left_or_right = input("Do you want to play left or right? (left/right)").lower()
        if left_or_right == "left":
            ans = input("Nice, you follow the path and reach a lake... Do you swim across or go around (across/around)?").lower()
            if ans == "across":
                defense -= 10
                print(f"You across the lake, you now have {defense} defense points and got bitten by a whale.")
                
            elif ans == "around":
                defense += 5
                print(f"you went around the lake, you now have {defense} defense points and reached the river.")
            else:
                print("Got you!! you lost.......")
        else:
            print("You fell down and lost.....")
    else:
        print(".....^^^^^^>>>>^^^...")
        
    
else:
    print(f"Sorry, Player {player.title()}, you are not eligible to play water and defense game!")