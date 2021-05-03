#!/usr/bin/env python
# coding: utf-8

# In[5]:


def show_table(mytable, choice, turn):
    #print("This is how the table looks with its position numbers:")
    #print("  1  |  2  |  3  \n  4  |  5  |  6  \n  7  |  8  |  9  ")
    if(turn % 2 == 0):
        mytable[choice - 1] = "o "
    else:
        mytable[choice - 1] = "x "
    for i in [0,3,6]:
        print(mytable[i] + "| " + mytable[i+1] + "| " + mytable[i+2])
    return mytable


# In[6]:


def accept_user_input(turn, all_inputs):
    p1 = "WRONG"
    within_range = False
    repeat_input = False
    
    while(p1.isdigit() == False or within_range == False or repeat_input == False):
        p1 = input("enter a number between 1-9: ")
        
        if(p1.isdigit() == False):
            print("sorry this is not a digit!")
        else:
            if(int(p1) in range(1,10)):
                within_range = True
            else:
                print("sorry this isn't in the valid range")
                print("enter number between 1 and 9")
        if(p1 in all_inputs):
            print("sorry this space is already occupied!try entering a different number")
            repeat_input = False
        elif(within_range == True and p1.isdigit() == True):
            repeat_input = True
            all_inputs.append(p1)
            print(f"list of inputs: {all_inputs}")
            turn += 1
            
    return(int(p1), turn)


# In[18]:


def masterfunc():
    print("welcome to tic tac toe!\n this is how the positions look with the numbers:")
    print("  1  |  2  |  3  \n  4  |  5  |  6  \n  7  |  8  |  9\n\n")
    mytable = ["_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ ", "_ "]
    turn = 0
    moves_made = []
    choice, turn = accept_user_input(turn, moves_made)
    tic_tac_toe_table = show_table(mytable, choice, turn)
    
    for i in range(2,10):
        choice, turn = accept_user_input(turn, moves_made)
        print(f"\n-----TURN {i} OVER-----\n")
        tic_tac_toe_table = show_table(tic_tac_toe_table, choice, turn)
        if(turn > 3):
            result_of_game = check_for_winner(tic_tac_toe_table)
            if(result_of_game == "game_over"):
                print("YOU WIN! GAME OVER")
                break
            elif(i == 9):
                print("it is a tie!")
    


# In[19]:


def check_for_winner(table):
    result = ""
    for i in [0,3,6]:
        if(table[i] == table[i+1] and table[i+1] == table[i+2] and table[i] != "_ "):
            print("game over, you have won!")
            result = "game_over"
            print(f"{i}, {i+1}, {i+2}")
            break 
    for i in [0,1,2]:
        if(table[i] == table[i+3] and table[i+3] == table[i+6] and table[i] != "_ "):
            print("game over, you have won!")
            result = "game_over"
            print(f"{i}, {i+3}, {i+6}")
            break 
    if(table[0] == table[4] and table[4] == table[8] and table[0] != "_  "):
        print("game over, you have won!")
        result = "game_over"
    if(table[2] == table[4] and table[4] == table[6] and table[2] != "_ "):
        print("game over, you have won!")
        result = "game_over"
    
    return result 


# In[ ]:


masterfunc()


# In[ ]:




