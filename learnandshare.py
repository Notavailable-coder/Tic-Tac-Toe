game_still_on = True

# Board General Structure
board = ["-" , "-" , "-" ,
         "-", "-" , "-",
         "-" , "-" , "-"]

#Displaying a Board
def display_board():
    print(board[0] + " | " + board[1] + " | "+ board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])



#who won
Winner = None

#whose turn is this
current_player = "X"

#Playing a game

def playing_game():
    display_board()

    while game_still_on:
        Handling_turn(current_player)
        check_if_game_over()

        Flip_players()


#checking the winner last time
        
    if winner == "X" or winner == "O":
        print(winner +" won.")
    elif winner == None:
        print("Tie.")

        
    


def Handling_turn(player):
    #Taking input from a user

    print(player +"'s Turn.")
   #Preventing overwriing filled vako place determine garne 
    valid = False
    while not valid:
    

        position = input ("Choose a position from 1-9:  ")
#Preventing from invalid inputs like overrange and other than integers
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:

            #warning pop out 
            position = input ("Invalid Entry ! Choose a position from 1-9:  ")


    #matching value of position with board value

    
        position = int(position)-1

        if board[position] == "-":
            valid =True
        else:
            print ("Place already filled ! Choose next position:")


    board[position] = player
    
    display_board()


def check_if_game_over():
    check_if_win()
    check_if_tie()




def check_if_win():

#linking global variable inside function 
    global winner
    
    #check_rows()
    row_winner = check_rows()
    
    #check_columns()
    columns_winner = check_columns()

    #check_diagonals()
    diagonals_winner = check_diagonals()



    if row_winner:
        #value returned from row_winner function
         winner = row_winner

    elif columns_winner:
        #value returned from columns_winner function
        winner = columns_winner

    elif diagonals_winner:
        #value returned from check_diagonals function
        winner = diagonals_winner

    else:

        #if winner are neither of the rows ,columns or diagonals
        winner = None
    return



def check_if_tie():
    # Defining global variable inside a function

    global game_still_on
    

    if "-" not in board:
        game_still_on =False
        
    return



def check_rows():

# Relaing the global variable once more
    global game_still_on

    #checking rows for the winner
    row_1 = board[0] == board[1] ==board[2] != "-"
    row_2 = board[3] == board[4] ==board[5] != "-"
    row_3 = board[6] == board[7] ==board[8] != "-"



#game over if we have already got the winner
    if row_1 or row_2 or row_3 :
        game_still_on = False

#Returning who is the winner 
    if row_1:
        return board[0]

    elif row_2:
        return board[3]


    elif row_3:
        return board[6]


    




    return
def check_columns():

    #relaing the global variable once more
    global game_still_on

    #checking columns for the winner
    columns_1 = board[0] == board[3] ==board[6] != "-"
    columns_2 = board[1] == board[4] ==board[7] != "-"
    columns_3 = board[2] == board[5] ==board[8] != "-"



#game over if we have already got the winner
    if columns_1 or columns_2 or columns_3 :
        game_still_on = False

#Returning who is the winner 
    if columns_1:
        return board[0]

    elif columns_2:
        return board[2]


    elif columns_3:
        return board[3]

    return


def check_diagonals():
        #relaing the global variable once more
    global game_still_on

    #checking diagonals for the winner
    diagonals_1 = board[0] == board[4] ==board[8] != "-"
    diagonals_2 = board[2] == board[4] ==board[6] != "-"


    #game over if we have already got the winner
    if diagonals_1 or diagonals_2 :
        game_still_on = False

#Returning who is the winner 
    if diagonals_1:
        return board[0]

    elif diagonals_2:
        #Returning the winner 
        return board[2]


    




    return

def Flip_players():
#Relating the global variable within a function
    global current_player


#fliping turn if presengt player was X next to be O. 
    if current_player == "X":
        current_player = "O"
#fliping turn if presengt player was O next to be X.
    elif current_player == "O":
        current_player ="X"
        
    return
#Executing a game actually playing the game::


playing_game()

