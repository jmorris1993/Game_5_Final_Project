#
# client for tic-tac-toe game (computer player)
#
# start passing in X or O as first argument, and the port
# to which to connect as second argument.
# (If first player to connect, connect as X. If second, connect as O.
# Getting this wrong will lead to strange behavior...)
#
# Minimax with alpha-beta search implementation
#

import sys
import socket


WIN_SEQUENCES = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6]
]

MARK_VALUE = {
    'O': 1,
    '.': 0,
    'X': 10
}


def has_win (board):
    for positions in WIN_SEQUENCES:
        s = sum(MARK_VALUE[board[pos]] for pos in positions)
        if s == 3:
            return 'O'
        if s == 30:
            return 'X'
    return False

def done (board):
    return (has_win(board) or not [ e for e in board if (e == '.')])



# 1 = X
# -1 = O

def utility (board):
    winner = has_win(board)
    if winner == 'O':
        return -1
    if winner == 'X':
        return 1
    return 0


def make_move (board,move,mark):
    # returns a copy of the board with the move recorded
    new_board = board[:]
    new_board[move] = mark
    return new_board

def other (player):
    if player == 'X':
        return 'O'
    if player == 'O':
        return 'X'
    return player

def alphabeta (board,player,alpha,beta):
    a = alpha
    b = beta
    if done(board):
        return utility(board)
    possible_moves = [i for (i,e) in enumerate(board) if e == '.']
    if player == 'X':
        for m in possible_moves:
            a = max(a,alphabeta(make_move(board,m,player),other(player),a,b))
            if b <= a:
                break
        return a
    if player == 'O':
        for m in possible_moves:
            b = min(b,alphabeta(make_move(board,m,player),other(player),a,b))
            if b <= a:
                break
        return b
    fail('unknown player '+player)

def value (board,player):
    return alphabeta(board,player,-2,2)

def computer_move (board,player):
    possible_moves = [i for (i,e) in enumerate(board) if e == '.']
    print possible_moves
    boards = [make_move(board,m,player) for m in possible_moves]
    values = [value(b,other(player)) for b in boards]
    print values
    if player == 'O': 
        target_val = min(values)
    if player == 'X':
        target_val = max(values)
    print 'Target value =', target_val
    for m in possible_moves:
        v = value(make_move(board,m,player),other(player))
        print 'Examining move',m,'with value',v
        if v == target_val:
            print 'Computer plays',m
            return m
    fail('Error: no move with value '+str(target_val))




# send a string on a socket 
# (keep sending until string fully sent)
def full_send (sock,msg):
    length = len(msg)
    totalsent = 0
    while totalsent < length:
        sent = sock.send(msg[totalsent:])
        if sent == 0:
            raise RuntimeError("socket connection broken")
        totalsent = totalsent + sent

# read a given number of characters from a socket
# (keep reading until all wanted characters received)
def full_receive (sock,length):
    chunks = []
    bytes_recd = 0
    while bytes_recd < length:
        chunk = sock.recv(min(length - bytes_recd, 2048))
        if chunk == '':
            raise RuntimeError("socket connection broken")
        chunks.append(chunk)
        bytes_recd = bytes_recd + len(chunk)
    return ''.join(chunks)


def send_move (sock,move):
    full_send (sock,str(move))


def recv_move (sock,board):
    valid = [ i for (i,e) in enumerate(board) if e == '.']
    input = full_receive(sock,1)
    move = input[0]
    if move in ["0","1","2","3","4","5","6","7","8"] and int(move) in valid:
        return int(move)
    return None



def main (player,port):

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("localhost",port))

    board = ['.'] * 9
    
    while not done(board):
        if (player=="X"):
            move = computer_move(board,"X")
            send_move(s,move)
        else:
            move = recv_move(s,board)
            print player+": move", move, "received"
        board[move] = "X"
        if not done(board):
            if (player=="O"):
                move = computer_move(board,"O")
                send_move(s,move)
            else:
                move = recv_move(s,board)
                print player+": move", move, "received"
            board[move] = "O"


if __name__ == '__main__':
    if len(sys.argv) > 2:
        main(sys.argv[1], int(sys.argv[2]))
    else:
        print "Need a player and port number"
