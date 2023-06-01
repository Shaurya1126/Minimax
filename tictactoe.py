import random
board = {1:" ",2:' ',3:' ',4:' ',5:' ',6:' ',7:' ', 8:' ', 9:' '}
def print_board():
    print(board[1],"I",board[2],'I',board[3])
    print("------------")
    print(board[4],"I",board[5],'I',board[6])
    print("------------")
    print(board[7],"I",board[8],'I',board[9])

def draw():
    for i in range(1,10):
        if board[i]==" ":
            return False
    return True

def win(move):
    if board[1]==move and board[2]==move and board[3]==move:
        return True
    if board[4]==move and board[5]==move and board[6]==move:
        return True
    if board[7]==move and board[8]==move and board[9]==move:
        return True
    if board[1]==move and board[5]==move and board[9]==move:
        return True
    if board[3]==move and board[5]==move and board[7]==move:
        return True
    if board[1]==move and board[4]==move and board[7]==move:
        return True
    if board[2]==move and board[5]==move and board[8]==move:
        return True
    if board[3]==move and board[6]==move and board[9]==move:
        return True
    return False
def insert(move):
    if win(move)==True:
        print_board()
        print(move, "wins!")
        exit()
    elif draw()==True:
        print_board()
        print("It's a draw")
        exit()
    else:
        if move==p1:
            x=int(input("Enter the position: "))
        elif move==p2:
            x=random.randint(1,9)
        if board[x]==" ":
            board[x]=move
            if win(move)==True:
                print(move, "wins!")
                exit()
        else:
            if move==p1:
                print('That position is already taken!')
                insert(move)
            else:
                insert(move)
                
    print()

p1=input("Would you like to play as X or O: ")
if p1=='X':
    p2="O"
else: 
    p2='X'
print_board()
while True:
    insert(p1)
    print_board()
    insert(p2)
    print_board()
    
    