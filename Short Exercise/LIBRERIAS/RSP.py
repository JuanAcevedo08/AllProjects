print("Welcome to The Game")
print("Turn of Player1")
Player1 = input("Choose between rock, paper, or scissors: ")
print("Turn of Player2")
Player2 = input("Choose rock, paper, or scissors: ")
is_Player1 = True
rock = "rock"
paper = "paper"
scissors = "scissors"

if is_Player1:
    if Player1 == rock and Player2 == scissors:
        print("Player1 Wins 🤖")
    elif Player1 == paper and Player2 == rock:
        print("Player1 Wins 🤖")
    elif Player1 == scissors and Player2 == paper:
        print("Player1 Wins 🤖")
    elif Player1 == Player2:
        print("It's a Tie!!")
    else:
        print("Player1 Lost 😭")

