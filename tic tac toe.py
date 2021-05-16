#TIC TAC TOE 

#This function prints table for every move made 
def show_table(mytable, choice, turn):
    if(turn % 2 == 0):
        mytable[choice - 1] = "o "
    else:
        mytable[choice - 1] = "x "
    for i in [0,3,6]:
        print(mytable[i] + "| " + mytable[i+1] + "| " + mytable[i+2])
    return mytable


#Accepts user input
def accept_user_input(turn, all_inputs):
    p1 = "WRONG"
    within_range = False
    repeat_input = False
    
    while(p1.isdigit() == False or within_range == False or repeat_input == False):
        p1 = input("Enter a number between 1-9: ")
        
        if(p1.isdigit() == False):
            print("Sorry, this is not a digit!\n")
        else:
            if(int(p1) in range(1,10)):
                within_range = True
            else:
                print("Sorry, this isn't in the valid range!\n")
                print("Enter number between 1 and 9")
        if(p1 in all_inputs):
            print("Sorry this space is already occupied!Try entering a different number!\n")
            repeat_input = False
        elif(within_range == True and p1.isdigit() == True):
            repeat_input = True
            all_inputs.append(p1)
            print(f"List of inputs: {all_inputs}")
            turn += 1
            
    return(int(p1), turn)


#Checks whether input entered is valid or not, that is, a yes or a no
def valid_input(choice):
    choice = choice.capitalize()
    while True:
        if(choice == "Yes" or choice == "No"):
            break
        else:
            print("Sorry this is an invalid input!")
            choice = input("Enter Yes or No: ").capitalize()
    return choice 


def masterfunc():
    print("Welcome to tic tac toe!\n This is how the positions look with the numbers:")
    print("  1  |  2  |  3  \n  4  |  5  |  6  \n  7  |  8  |  9\n")
    mytable = ["_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ "]
    turn = 0
    moves_made = []
    choice, turn = accept_user_input(turn, moves_made)
    tic_tac_toe_table = show_table(mytable, choice, turn)
    
    for i in range(2,10):
        print(f"\n-------TURN {i}-------\n")
        choice, turn = accept_user_input(turn, moves_made)
        tic_tac_toe_table = show_table(tic_tac_toe_table, choice, turn)
        result_of_game = check_for_winner(tic_tac_toe_table)
        if(result_of_game == "game_over"):
            print("You win!\nGAME OVER\n")
            break
        elif(i == 9):
        	print("It is a tie!")


#Entails all possibilites of winning in this game and checks if that is the case
def check_for_winner(table):
    result = ""
    for i in [0,3,6]:
        if(table[i] == table[i+1] == table[i+2] and table[i] != "_ "):
            print("Game over, you have won!")
            result = "game_over"
            return result 
    for i in [0,1,2]:
        if(table[i] == table[i+3] == table[i+6] and table[i] != "_ "):
            print("Game over, you have won!")
            result = "game_over"
            return result
    if(table[0] == table[4] == table[8] and table[0] != "_ "):
        print("Game over, you have won!")
        result = "game_over"
        return result
    if(table[2] == table[4] == table[6] and table[2] != "_ "):
        print("Game over, you have won!")
        result = "game_over"
        return result 


while True:
    masterfunc()
    choice = input("Do you want to play once more?(Yes/No): ")
    choice = valid_input(choice)
    if choice == "No":
        print("Have a good day!")
        break
    
