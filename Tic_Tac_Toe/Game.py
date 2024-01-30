import random

def Greeting():
    print("\t****** Welcome To Tic Tac Toe ******\n")

x = [['1','2','3'],['4','5','6'],['7','8','9']]
no = ['1','2','3','4','5','6','7','8','9']
x_dic = {'1':(0,0),'2':(0,1),'3':(0,2),'4':(1,0),'5':(1,1),'6':(1,2),'7':(2,0),'8':(2,1),'9':(2,2)}

def show_board(x):
    print("-----------")
    for i in x:
        print(f"|{i[0]} | {i[1]} | {i[2]}|")
        print("-----------\n")

def reset_board():
    global x
    x = [['1','2','3'],['4','5','6'],['7','8','9']]

def check_win(x):

    for i in range(3):

        if (x[i][0] == x[i][1] == x[i][2]) and (x[i][0] == 'X' or x[i][0] == 'O') :
            return True
        
        elif (x[0][i] == x[1][i] == x[2][i]) and (x[0][i] == 'X' or x[0][i] == 'O'):
            return True
        
    if (x[0][0] == x[1][1] == x[2][2]) and (x[0][0] == 'X' or x[0][0] == 'O'):
        return True
            
    if (x[0][2] == x[1][1] == x[2][0]) and (x[2][0] == 'X' or x[2][0] == 'O'):
        return True
             
    return False

def board_full():
    global x
    for i in x:
        for j in i:
            if j in no:
                return False
    
    return True

def check_empty(y):
    if x[x_dic[y][0]][x_dic[y][1]] == y:
        return True
    return False

def assign_value(y,player):
    x[x_dic[y][0]][x_dic[y][1]] = player
    
def play():
    finished = False
    while True and not finished:
        player_1 = random.choice(['X','O'])
        player_2 = 'X' if player_1 == 'O' else 'O' 

        while True:
            temp = input("Player 1 Enter a number: ")

            if temp not in no:
                print("Invalid input, try again")
                continue
            else:
                if check_empty(temp):
                    assign_value(temp,player_1)
                    show_board(x)
            
                else:
                    print("The choosen number is occupied, try again")
                    continue

            if check_win(x):
                print("Player 1 Won")
                finished = True
                break
            else:
                if board_full():
                    print("Tie")
                    finished = True
                    break
                else:
                    break
        
        while True and not finished:
            temp = input("Player 2 Enter a number: ")

            if temp not in no:
                print("Invalid input, try again")
                continue
            else:
                if check_empty(temp):
                    assign_value(temp,player_2)
                    show_board(x)
            
                else:
                    print("The choosen number is occupied, try again")
                    continue

            if check_win(x):
                print("Player 2 Won")
                finished = True
                break
            else:
                if board_full():
                    print("Tie")
                    finished = True
                    break
                else:
                    break

def launch_game():
    
    while True:
        Greeting()
        show_board(x)
        play()
        ans = input("Do You want to play again? ").strip().lower()
        if ans != 'yes':
            print("Good Bye, See you soon ")
            break
        reset_board()