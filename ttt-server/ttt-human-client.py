#
# client for tic-tac-toe game (human player)
#
# start passing in X or O as first argument, and the port
# to which to connect as second argument.
# (If first player to connect, connect as X. If second, connect as O.
# Getting this wrong will lead to strange behavior...)
#

import sys
import socket
from graphics import *


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


def draw_board(win,board):

    brd=[board[0:3],board[3:6],board[6:9]]

    for i in range(110, 440, 110):
        for j in range(110, 440, 110):
            Rectangle(Point(i-100,j-100),Point(i,j)).draw(win)
    for i in range(3):
        for j in range(3):
            pt= Point((j+1)*110-50,(i+1)*110-50) 
            if brd[i][j] in ["X","O"]:
                txt = Text(pt,brd[i][j])
                txt.setSize(36)
                txt.draw(win)

def wait_player_input (win,board,player):
    moves=[[0,1,2],[3,4,5],[6,7,8]]
    pt = win.getMouse()
    x,y = (pt.getX(),pt.getY())

    for i in range(0, 330, 110):
        for j in range(0, 330, 110):
            if x>i+10 and x<i+110 and y>j+10 and y<j+110:
                return moves[j/110][i/110]



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

    win = GraphWin('TTT Client - Player '+player,350,400)

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("localhost",port))

    board = ['.'] * 9
    draw_board(win,board)
    
    while not done(board):
        if (player=="X"):
            move = wait_player_input(win,board,"X")
            send_move(s,move)
        else:
            move = recv_move(s,board)
            print player+": move", move, "received"
        board[move] = "X"
        draw_board(win,board)
        if not done(board):
            if (player=="O"):
                move = wait_player_input(win,board,"O")
                send_move(s,move)
            else:
                move = recv_move(s,board)
                print player+": move", move, "received"
            board[move] = "O"
            draw_board(win,board)

    win.close()


if __name__ == '__main__':
    if len(sys.argv) > 2:
        main(sys.argv[1], int(sys.argv[2]))
    else:
        print "Need a player and port number"
