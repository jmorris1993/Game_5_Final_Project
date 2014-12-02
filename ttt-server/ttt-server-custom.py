#
# Simple tic-tac-toe game as a server with custom clients
#
# - Start by passing in a port as an argument
#
# - Use either the ttt-human-client or ttt-computer-client to connect
#
# - Each of those clients is started with a first argument either X or O
#   indicating what the client is playing as (the first client should be X
#   the second should be O) and the port to which to connect and on which 
#   the server is listening.
#
# - Two players need to connect for the game to start
#
# - A move is a position [0-8]



import sys
import socket

def fail (msg):
    raise StandardError(msg)


# representation 9-cells array, each cell 1 'O','.','X'

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

def initialize_board ():
    return ['.'] * 9

def has_win (board):
    for positions in WIN_SEQUENCES:
        s = sum(MARK_VALUE[board[pos]] for pos in positions)
        if s == 3:
            return 'O'
        if s == 30:
            return 'X'
    return False

def print_board (board):
    for i in range(0,3):
        print '  ',board[i*3],board[i*3+1],board[i*3+2]
    print

def done (board):
    return (has_win(board) or not [ e for e in board if (e == '.')])



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

def send_move (psock, move):
    full_send (psock,str(move))

def recv_move (psock,board):
    valid = [ i for (i,e) in enumerate(board) if e == '.']
    input = full_receive(psock,1)
    if input == "q":
        return "quit"
    move = input[0]
    if move in ["0","1","2","3","4","5","6","7","8"] and int(move) in valid:
        return int(move)
    return None

def play (p1sock,p2sock):

    board = initialize_board()

    print_board(board)

    while not done(board):
        move = recv_move(p1sock,board)
        if move == "quit":
            return
        board[move] = 'X'
        print_board(board)
        send_move(p2sock,move)
        if not done(board):
            move = recv_move(p2sock,board)
            if move == "quit":
                return
            board[move] = 'O'
            print_board(board)
            send_move(p1sock,move)

    winner = has_win(board)
    if winner:
        print winner,'wins!'
    else:
        print 'Draw'

        
def main(port):

    # Create a listening socket to listen for connection attempts
    serversocket = socket.socket(socket.AF_INET, 
                                 socket.SOCK_STREAM)
    serversocket.bind(('',port))
    serversocket.listen(2)

    while True:
        # wait for two players to connect
        print "Waiting for first player"
        (player1socket,address1) = serversocket.accept()
        print "Waiting for second player"
        (player2socket,address2) = serversocket.accept()
        play(player1socket,player2socket)
        player1socket.close()
        player2socket.close()
        

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        print "Need a port number"
