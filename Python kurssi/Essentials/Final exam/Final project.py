from random import randrange
row1 = [1, 2, 3]
row2 = [4, 5, 6]
row3 = [7, 8, 9]
board = [row1, row2, row3]

global finish
finish = False

def display_board(board):
  print('+-------+-------+-------+\n|       |       |       |')
  print('|  ',board[0][0],'  |  ',board[0][1],'  |  ',board[0][2],'  |')
  print('|       |       |       |')
  print('+-------+-------+-------+\n|       |       |       |')
  print('|  ',board[1][0],'  |  ',board[1][1],'  |  ',board[1][2],'  |')
  print('|       |       |       |')
  print('+-------+-------+-------+\n|       |       |       |')
  print('|  ',board[2][0],'  |  ',board[2][1],'  |  ',board[2][2],'  |')
  print('|       |       |       |\n+-------+-------+-------+')
display_board(board)

def enter_move(board):
  user_move = int(input('Enter your move: '))
  if user_move in row1:
    i = row1.index(user_move)
    row1[i] = 'O'
  elif user_move in row2:
    i = row2.index(user_move)
    row2[i] = 'O'
  elif user_move in row3:
    i = row3.index(user_move)
    row3[i] = 'O'
  display_board(board)

def make_list_of_free_fields(board):
  global free_squares_list
  free_squares_list = []
  for row in range(len(board)):
    for col in range (len(board[row])):
      if board[row][col] != 'X' and board[row][col] != 'O':
        free_squares_list.append((row, col))

make_list_of_free_fields(board)
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


def victory_for(board):
  global finish
  #finish = False
  if board[0] == ['X', 'X', 'X'] or board[1] == ['X', 'X', 'X'] or board[2] == ['X', 'X', 'X'] or\
    board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X' or \
    board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X' or \
    board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X'or \
    board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X' or \
    board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X' or \
    board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
    print('You lose!')
    finish = True
    return finish
  elif board[0] == ['O', 'O', 'O'] or board[1] == ['O', 'O', 'O'] or board[2] == ['O', 'O', 'O'] or\
    board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O' or \
    board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O' or \
    board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O'or \
    board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O' or \
    board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O' or \
    board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':
    print('You won!')
    finish = True
    return finish
  elif len(free_squares_list) == 0:
    print('Draw!')
    finish = True
    return finish
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game


def draw_move(board):
  global finish
  while not finish:
      i = len(free_squares_list)
      if i == 0:
        print('Draw!')
        finish = True
        break
      if i == 9:
        board[1][1] = 'X'
        display_board(board)
      else:
        index = randrange(i) - 1
        tuple = free_squares_list[index]
        board[tuple[0]][tuple[1]] = 'X'
        display_board(board)
      victory_for(board)
      if finish:
        break
      enter_move(board)
      if victory_for(board):
        break
      make_list_of_free_fields(board)
      # The function draws the computer's move and updates the board.
draw_move(board)