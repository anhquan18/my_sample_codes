import pygame, sys
from pygame.locals import *

#Game size
try:
    game_size, win_height, game_depth = int(sys.argv)
except Exception:
    game_size = 3
    win_height = (game_size * 100) - (game_size * 10)
    game_depth = 5

# Make win size for the game
if game_size >= 5:
    win_size = 5
else:
    win_size = 3

FPS = 60
win_width = win_height
box_size = 40
gap_size = 20
board_height = game_size
board_width = game_size
win_margin = (win_height - (box_size * board_height + gap_size * (board_height - 1))) / 2
o_win = -1000
x_win = 1000
tie = 1 
block = 500

# R G B
d_blue = (0, 0, 51)
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

# Player
X = 1
O = -1

# Game rule
assert game_size >= 3, "The size of the game is too small"
assert game_size *(box_size + gap_size) <= win_height, "The game size doesn't fit the display"
assert win_height <= 1000, "The size of the game is too big for the screen"


def main():
    pygame.init()
    global game_surf
    game_fps = pygame.time.Clock()
    mousex = 0
    mousey = 0
    x_o_turn = O 
    game_board = Create_board()
    
    game_surf = pygame.display.set_mode((win_width, win_height))
    pygame.display.set_caption('X O GAME')
    
    while True:
        game_surf.fill(white)
        Draw_board(game_board)
        pygame.display.update()
        
        if G_Won(game_board, True) == 'won':
            pygame.time.wait(2000)
            game_board = Create_board()
        elif G_Won(game_board) == 'tie':
            pygame.time.wait(3000)
            game_board = Create_board()
        
        
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                x_pos, y_pos = Find_pos(mousex, mousey)
                
                if x_pos != None and y_pos != None and game_board[x_pos][y_pos] == False:
                    game_board[x_pos][y_pos] = O 
                    x_o_turn *= -1
                    
                    empty_place = P_left(game_board)
                    x_moves = []
                    for i in empty_place:
                        x, y = i
                        game_board[x][y] = X
                        print game_board
                        print 'x: {}, y: {} depth: {} player: {}\n'.format(x, y, game_depth, X)
                        g_nod = G_node(X, game_depth, game_board, [x, y])
                        game_board[x][y] = False
                        x_moves.append(g_nod) 
                    best_val = (o_win, [])
                    for i in range(len(x_moves)):
                        game_node = x_moves[i]
                        normal_move = Min_max(game_node, game_depth)
                        print normal_move
                        if (normal_move[0] >= best_val[0]) and (normal_move[1] != []):
                            best_move = normal_move
                    print 'X chooses', best_move[1]
                    game_board[best_move[1][0]][best_move[1][1]] = X
        game_fps.tick(FPS)


class G_node:
    def __init__(self, player, depth, g_board, position = None):
        self.player = player
        self.depth = depth
        self.g_board = g_board
        self.pos = position
        self.state = self.State()
        self.n_moves = []
        self.Next_move()
    
    def Next_move(self):
        if (self.depth <= 0) or (G_Won(self.g_board) == 'won'):
            if (self.depth > 0) and self.player == X:
                self.state = x_win
            return 0
        if G_Won(self.g_board) == False:
            empty_b = P_left(self.g_board)
            for i in empty_b:
                x_pos, y_pos = i
                self.g_board[x_pos][y_pos] = -self.player
                print self.g_board
                print 'x: {}, y: {} depth: {} player: {} world_state: {}\n'.format(x_pos, y_pos, self.depth - 1, -self.player,self.state)
                n_node = G_node(-self.player, self.depth - 1, self.g_board, [x_pos, y_pos])
                self.g_board[x_pos][y_pos] = False
                self.n_moves.append(n_node)
    
    def State(self):
        if G_Won(self.g_board) == 'won':
            if self.player == O:
                print 'o won\n'
                return o_win 
            else:
                print 'x won\n'
                return x_win - self.depth
        elif G_Won == 'tie':
            return tie
        if Block(self.g_board, self.pos[0], self.pos[1]):
            print 'block worked\n'
            return block
        return 0


def Block(board, x_cor, y_cor):
    count = 0
    print x_cor, y_cor
    #Vertical block
    for x_pos in range(board_width):
        for y_pos in range(board_height - win_size + 1):
            print x_pos, y_pos
            for i in range(win_size - 1):
                if (board[x_pos][y_pos + i] == O) and (board[x_pos][y_pos + i] == board[x_pos][y_pos + i + 1]):
                    print 'counting\n'
                    count += 1
                if (count == game_size - 2) and (((board[x_pos][y_pos] == X) and (x_pos == x_cor and y_pos == y_cor)) or ((board[x_pos][y_pos + i + 1] == X) and (x_pos == x_cor and (y_pos + i + 1) == y_cor))):
                    return True
            count = 0
    #Side block 
    for y_pos in range(board_height):
        for x_pos in range(board_width - win_size + 1):
            for i in range(win_size - 1):
                if (board[x_pos + i][y_pos] == O) and (board[x_pos + i][y_pos] == board[x_pos + i + 1][y_pos]):
                    print 'counting\n'
                    count += 1
                if (count == game_size - 2) and (((board[x_pos][y_pos] == X) and ((x_pos == x_cor) and (y_pos == y_cor))) or ((board[x_pos + i + 1][y_pos] == X) and (((x_pos + i + 1) == x_cor) and (y_pos == y_cor)))):
                    return True
            count = 0
    #Diagonal
    for x_pos in range(int(win_size / 2), board_width - int(win_size / 2)):
        for y_pos in range(int(win_size / 2), board_height - int(win_size / 2)):
            #Lef to right 
            for i in range(int(win_size/2)):
                if (board[x_pos + i][y_pos + i] == board[x_pos + i + 1][y_pos + i + 1]) and (board[x_pos + i][y_pos + i] == O):
                    count += 1
                if (board[x_pos - i][y_pos - i] == board[x_pos - i - 1][y_pos - i - 1]) and (board[x_pos - i][y_pos - i] == O):
                    count += 1
                if (count == win_size - 2) and ((board[x_pos + i + 1][y_pos + i + 1] == X and (x_cor == (x_pos + i + 1) and y_cor == (y_pos + i + 1))) or (board[x_pos - i - 1][y_pos - i - 1] == X and (x_cor == (x_pos - i - 1) and y_cor == (y_pos - i - 1)))):
                    return True
            count = 0
            #Right to left 
            for i in range(int(win_size/2)):
                if (board[x_pos + i][y_pos - i] == board[x_pos + i + 1][y_pos - i - 1]) and (board[x_pos + i][y_pos - i] == O):
                    count += 1
                if (board[x_pos - i][y_pos + i] == board[x_pos - i - 1][y_pos + i + 1]) and (board[x_pos - i][y_pos + i] == O):
                    count += 1
                if (count == win_size - 2) and ((board[x_pos + i + 1][y_pos - i - 1] == X and (x_cor == (x_pos + i + 1) and y_cor == (y_pos - i - 1))) or (board[x_pos - i - 1][y_pos + i + 1] == X and (x_cor == (x_pos - i - 1) and y_cor == (y_pos + i + 1)))):
                    return True
            count = 0
    return False


def Min_max(node, depth):
    if (abs(node.state) == x_win) or (depth == 0):
        return (node.state, node.pos)
    
    b_val = (o_win, [])
    for i in range(len(node.n_moves)):
        game_node = node.n_moves[i]
        n_val = Min_max(game_node, depth - 1)
        if (n_val[0] >= b_val[0]):
            b_val = n_val
    return b_val

def P_left(board):
    empty_b = []
    for x_cor in range(board_width):
        for y_cor in range(board_height):
            if board[x_cor][y_cor] == False:
                empty_b.append((x_cor, y_cor))
    return empty_b


def Won_anime(x, y, win_size, won_type):
    x_pix, y_pix = Get_x_y_pixel(x, y)
    
    l_speed = box_size / 10
    half = box_size / 2
    l_width = gap_size / 8
    speed_rate = (box_size + gap_size) / l_speed
    
    for i in range(1, (win_size * speed_rate) + 1):
        if won_type == 'side':
            pygame.draw.line(game_surf, d_blue, (x_pix - gap_size, y_pix + half), (x_pix + (i * l_speed), y_pix + half), l_width)
        if won_type == 'vertical':
            pygame.draw.line(game_surf, d_blue, (x_pix + half, y_pix - gap_size), (x_pix + half, y_pix + (i * l_speed)), l_width)
        if won_type == 'diagonal_left':
            pygame.draw.line(game_surf, d_blue, (x_pix + half - (i * l_speed) / 2, y_pix + half - (i * l_speed) / 2), (x_pix + half + (i * l_speed) / 2, y_pix + half + (i * l_speed) / 2), l_width)
        if won_type == 'diagonal_right':
            pygame.draw.line(game_surf, d_blue, (x_pix + half - (i * l_speed) / 2, y_pix + half + (i * l_speed) / 2), (x_pix + half + (i * l_speed) / 2, y_pix + half - (i * l_speed) / 2), l_width)
        
        pygame.display.update()
        # Wait 22 milisecond for smoother animation 
        pygame.time.wait(22)


def G_Won(board, ani = False):
    won_type = [False, False, [False,False]]
    x_count = 0
    o_count = 0
    
    # VERTICAL WIN
    for x_cor in range(board_width):
        for y_cor in range(board_height - win_size + 1):
            for i in range(win_size - 1):
                if board[x_cor][y_cor + i] == board[x_cor][y_cor + i + 1]:
                    if board[x_cor][y_cor] == X:
                        x_count += 1
                    elif board[x_cor][y_cor] == O:
                        o_count += 1
                if (x_count == win_size - 1) or (o_count == win_size - 1):
                    won_type = ['won','vertical',(x_cor, y_cor)]
            x_count = 0
            o_count = 0
    
    # SIDE WIN
    for y_cor in range(board_height):
        for x_cor in range(board_width - win_size + 1):
            for i in range(win_size - 1):
                if board[x_cor + i][y_cor] == board[x_cor + i + 1][y_cor]:
                    if board[x_cor][y_cor] == X:
                        x_count += 1
                    elif board[x_cor][y_cor] == O:
                        o_count += 1
                if (x_count == win_size - 1) or (o_count == win_size - 1):
                    won_type = ['won','side',(x_cor, y_cor)]
            x_count = 0
            o_count = 0
    
    # DIAGONAL WIN
    for x_cor in range(int(win_size / 2), board_width - int(win_size / 2)):
        for y_cor in range(int(win_size / 2), board_height - int(win_size / 2)):
            # LEFT TO RIGHT
            for i in range(int(win_size / 2)):
                if board[x_cor + i][y_cor + i] == board[x_cor + i + 1][y_cor + i + 1]:
                    if board[x_cor][y_cor] == X:
                        x_count += 1
                    if board[x_cor][y_cor] == O:
                        o_count += 1
                if board[x_cor - i][y_cor - i] == board[x_cor - i - 1][y_cor - i - 1]:
                    if board[x_cor][y_cor] == X:
                        x_count += 1
                    if board[x_cor][y_cor] == O:
                        o_count += 1
                if (x_count == win_size - 1) or (o_count == win_size - 1):
                    won_type = ['won','diagonal_lef',(x_cor, y_cor)]
            x_count = 0
            o_count = 0
            
            # RIGHT TO LEFT
            for i in range(int(win_size / 2)):
                if board[x_cor - i][y_cor + i] == board[x_cor - i - 1][y_cor + i + 1]:
                    if board[x_cor][y_cor] == X:
                        x_count += 1
                    if board[x_cor][y_cor] == O:
                        o_count += 1
                if board[x_cor + i][y_cor - i] == board[x_cor + i + 1][y_cor - i - 1]:
                    if board[x_cor][y_cor] == X:
                        x_count += 1
                    if board[x_cor][y_cor] == O:
                        o_count += 1
                if (x_count == win_size - 1) or (o_count == win_size - 1):
                    won_type = ['won','diagonal_right',(x_cor, y_cor)]
            x_count = 0
            o_count = 0
   #game_surf.fill(white)
   #Draw_board(board)
   #pygame.display.update()
    
    if (won_type[0] == 'won') and (ani == True):
        Won_anime(won_type[2][0], won_type[2][1], win_size, won_type[1])
        return 'won'
    
    if (won_type[0] == 'won'):
        return 'won'
    
    for x in range(board_width):
        for y in range(board_height):
            if board[x][y] == False:
                return False
    return 'tie'


def Make_2d_list(board):
    n_list = []
    for x_cor in range(0, len(board), game_size):
        n_list.append(board[x_cor:(x_cor + game_size)])
    return n_list


def Find_pos(x, y):
    for x_cor in range(board_width):
        for y_cor in range(board_height):
            x_pix, y_pix = Get_x_y_pixel(x_cor, y_cor)
            x_y_check = pygame.Rect(x_pix, y_pix, box_size, box_size)
            if x_y_check.collidepoint(x, y):
                return (x_cor, y_cor)
    return (None, None)


def Draw_board(board):
    half = gap_size / 2
    # Draw gap first then draw x o
    for x_cor in range(1, board_width):
        pygame.draw.line(game_surf, black, ((win_margin + x_cor * (box_size + gap_size)) - half, win_margin), ((win_margin + x_cor * (box_size + gap_size)) - half, win_height - win_margin), half - 8)
    for y_cor in range(1, board_height):
        pygame.draw.line(game_surf, black, (win_margin,(win_margin + y_cor * (box_size + gap_size)) - half), (win_width - win_margin, (win_margin + y_cor * (box_size + gap_size)) - half), half - 8)
    for x_cor in range(board_width):
        for y_cor in range(board_height):
            if board[x_cor][y_cor] == O:
                Draw_x_o(O, x_cor, y_cor)
            elif board[x_cor][y_cor] == X:
                Draw_x_o(X, x_cor, y_cor)


def Create_board():
    board = []
    for x in range(board_width):
        for y in range(board_height):
            board.append(False)
    board = Make_2d_list(board)
    return board


def Get_x_y_pixel(x, y):
    x_pix_cor = x * (box_size + gap_size) + win_margin
    y_pix_cor = y * (box_size + gap_size) + win_margin
    return (x_pix_cor, y_pix_cor)


def Draw_x_o(sign, x, y):
    x_pix, y_pix = Get_x_y_pixel(x,y)
    half = box_size / 2
    
    if sign == X:
        pygame.draw.line(game_surf, black, (x_pix, y_pix),(x_pix + box_size, y_pix + box_size))
        pygame.draw.line(game_surf, black, (x_pix, y_pix + box_size),(x_pix + box_size, y_pix))
    
    elif sign == O:
        pygame.draw.circle(game_surf, red, (x_pix + half, y_pix + half), half, half - 18)


if __name__ == '__main__':
    main()
