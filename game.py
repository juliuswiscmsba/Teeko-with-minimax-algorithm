import random
import copy

class TeekoPlayer:
    """ An object representation for an AI game player for the game Teeko.
    """
    board = [[' ' for j in range(5)] for i in range(5)]
    pieces = ['b', 'r']

    def __init__(self):
        """ Initializes a TeekoPlayer object by randomly selecting red or black as its
        piece color.
        """
        self.my_piece = random.choice(self.pieces)
        self.opp = self.pieces[0] if self.my_piece == self.pieces[1] else self.pieces[1]

    def check_position(self, state):
        my_piece = []
        oppo_piece = []
        for i in range(5):
            for j in range(5):
                if state[i][j] == self.my_piece:
                    my_piece.append((i,j))
                if state[i][j] == self.opp:
                    oppo_piece.append((i,j))
        return my_piece, oppo_piece
    
    def check_status(self, state):
        count = 0
        for i in range(5):
            for j in range(5):
                if state[i][j] != ' ':
                    count +=1
        print(count)
        if count < 8:
            return True
        else:
            return False
        
    def heuristic_game_value(self, state):
        my_piece, oppo_piece = self.check_position(state)
        
        my_sim_max = 0
        oppo_sim_max = 0
        
        #check horizontal
        my_cnt = 0
        oppo_cnt = 0
        for r,c in my_piece:
            my_sim_count = 0
            for k in range(5):
                if state[r][k] == self.my_piece:
                    my_sim_count+=1
                if state[r][k] == self.opp:
                    my_sim_count=0
                    break;
            if my_cnt < my_sim_count:
                my_cnt = my_sim_count
            
        for r,c in oppo_piece:
            oppo_sim_count = 0
            for k in range(5):
                if state[r][k] == self.opp:
                    oppo_sim_count+=1
                if state[r][k] == self.my_piece:
                    oppo_sim_count=0
                    break;
            if oppo_cnt < oppo_sim_count:
                oppo_cnt = oppo_sim_count
        
        if my_cnt > my_sim_max:
            my_sim_max = my_cnt
        if oppo_cnt > oppo_sim_max:
            oppo_sim_max = oppo_cnt
            
        #check vertical
        my_cnt = 0
        oppo_cnt = 0
        for r,c in my_piece:
            my_sim_count = 0
            for k in range(5):
                if state[k][c] == self.my_piece:
                    my_sim_count+=1
                if state[k][c] == self.opp:
                    my_sim_count=0
                    break;
            if my_cnt < my_sim_count:
                my_cnt = my_sim_count
            
        for r,c in oppo_piece:
            oppo_sim_count = 0
            for k in range(5):
                if state[k][c] == self.opp:
                    oppo_sim_count+=1
                if state[k][c] == self.my_piece:
                    oppo_sim_count=0
                    break;
            if oppo_cnt < oppo_sim_count:
                oppo_cnt = oppo_sim_count
        
        if my_cnt > my_sim_max:
            my_sim_max = my_cnt
        if oppo_cnt > oppo_sim_max:
            oppo_sim_max = oppo_cnt
        
        #check \
        my_cnt = 0
        oppo_cnt = 0
        for i,j in my_piece:
            my_sim_count = 1
            for temp in range(1,4):
                if i+temp < 5 and j+temp<5:
                    if (i+temp, j+temp) in my_piece:
                        my_sim_count+=1
                if i-temp >= 0 and j-temp >= 0:
                    if (i-temp, j-temp) in my_piece:
                        my_sim_count+=1
                        
            for temp in range(1,4):
                if i+temp < 5 and j+temp<5:
                    if (i+temp, j+temp) in oppo_piece:
                        my_sim_count=0
                        break;
                if i-temp >= 0 and j-temp >= 0:
                    if (i-temp, j-temp) in oppo_piece:
                        my_sim_count=0
                        break;                        
                        
            if my_cnt < my_sim_count:
                my_cnt = my_sim_count 
                
        for i,j in oppo_piece:
            oppo_sim_count = 1
            for temp in range(1,4):
                if i+temp < 5 and j+temp<5:
                    if (i+temp, j+temp) in oppo_piece:
                        oppo_sim_count+=1
                if i-temp >= 0 and j-temp >= 0:
                    if (i-temp, j-temp) in oppo_piece:
                        oppo_sim_count+=1

            for temp in range(1,4):
                if i+temp < 5 and j+temp<5:
                    if (i+temp, j+temp) in my_piece:
                        oppo_sim_count=0
                        break;
                if i-temp >= 0 and j-temp >= 0:
                    if (i-temp, j-temp) in my_piece:
                        oppo_sim_count=0 
                        break;
                        
            if oppo_cnt < oppo_sim_count:
                oppo_cnt = oppo_sim_count                 
                
        if my_cnt > my_sim_max:
            my_sim_max = my_cnt
        if oppo_cnt > oppo_sim_max:
            oppo_sim_max = oppo_cnt        
        #check /
        my_cnt = 0
        oppo_cnt = 0
        for i,j in my_piece:
            my_sim_count = 1
            for temp in range(1,4):
                if i+temp < 5 and j-temp>=0:
                    if (i+temp, j-temp) in my_piece:
                        my_sim_count+=1
                if i-temp >= 0 and j+temp < 5:
                    if (i-temp, j+temp) in my_piece:
                        my_sim_count+=1
                        
            for temp in range(1,4):
                if i+temp < 5 and j-temp>=0:
                    if (i+temp, j-temp) in oppo_piece:
                        my_sim_count=0
                        break;
                if i-temp >= 0 and j+temp < 5:
                    if (i-temp, j+temp) in oppo_piece:
                        my_sim_count=0
                        break;
            
            if my_cnt < my_sim_count:
                my_cnt = my_sim_count 
                
        for i,j in oppo_piece:
            oppo_sim_count = 1
            for temp in range(1,4):
                if i+temp < 5 and j-temp>=0:
                    if (i+temp, j-temp) in oppo_piece:
                        oppo_sim_count+=1
                if i-temp >= 0 and j+temp < 5:
                    if (i-temp, j+temp) in oppo_piece:
                        oppo_sim_count+=1
                        
            for temp in range(1,4):
                if i+temp < 5 and j-temp>=0:
                    if (i+temp, j-temp) in my_piece:
                        oppo_sim_count = 0
                        break;
                if i-temp >= 0 and j+temp < 5:
                    if (i-temp, j+temp) in my_piece:
                        oppo_sim_count = 0
                        break;
            if oppo_cnt < oppo_sim_count:
                oppo_cnt = oppo_sim_count                 
                
        if my_cnt > my_sim_max:
            my_sim_max = my_cnt
        if oppo_cnt > oppo_sim_max:
            oppo_sim_max = oppo_cnt   
        #check 2*2
        my_cnt = 0
        oppo_cnt = 0
        
        
        for r in range(4):
            for c in range(4):
                my_sim_count = 0
                if state[r][c] == self.my_piece:
                    my_sim_count+=1
                    if state[r+1][c] == self.my_piece:
                        my_sim_count+=1
                    if state[r][c+1] == self.my_piece:
                        my_sim_count+=1
                    if state[r+1][c+1] == self.my_piece:
                        my_sim_count+=1
                    if state[r+1][c] == self.opp or state[r][c+1] == self.opp or state[r+1][c+1] == self.opp:
                        my_sim_count=0
                    if my_cnt < my_sim_count:
                        my_cnt = my_sim_count
        
        for r in range(4):
            for c in range(4):
                oppo_sim_count = 0
                if state[r][c] == self.opp:
                    oppo_sim_count+=1
                    if state[r+1][c] == self.opp:
                        oppo_sim_count+=1
                    if state[r][c+1] == self.opp:
                        oppo_sim_count+=1
                    if state[r+1][c+1] == self.opp:
                        oppo_sim_count+=1
                    if state[r+1][c] == self.my_piece or state[r][c+1] == self.my_piece or state[r+1][c+1] == self.my_piece:
                        oppo_sim_count=0
                    if oppo_cnt < oppo_sim_count:
                        oppo_cnt = oppo_sim_count       
        
                
        if my_cnt > my_sim_max:
            my_sim_max = my_cnt
        if oppo_cnt > oppo_sim_max:
            oppo_sim_max = oppo_cnt 
        

        return (my_sim_max-oppo_sim_max)/4, state
        
    def succ(self, state, piece):
        turn = piece
        curr_state = copy.deepcopy(state)
        count = 0
        for q in range(5):
            for p in range(5):
                if state[q][p] != ' ':
                    count+=1
        if count <8 :
            drop_phase = True
        
        else:
            drop_phase = False
            
        if drop_phase:
            all_succ_list=[]
            for r in range(5):
                for c in range(5):
                    if state[r][c] == ' ':
                        succ_state = copy.deepcopy(curr_state)
                        succ_state[r][c] = turn
                        all_succ_list.append(succ_state)
            
        else:                        
            piece_list = []
            for i in range(5):
                for j in range(5):
                    if state[i][j] == turn:
                        piece_list.append((i,j))
                        
            all_succ_list=[]
           
            for r,c in piece_list:
                for t in (-1,0,1):
                    for k in (-1,0,1):
                        if r+t >= 0 and c+k >=0 and r+t <5 and c+k <5 and curr_state[r+t][c+k] == " ":
                            temp_state = copy.deepcopy(curr_state)
                            temp_state[r][c] = ' '
                            temp_state[r+t][c+k] = turn
                            all_succ_list.append(temp_state)
            
    
        return all_succ_list
                            
    
    def max_value(self, state, depth):
        new_state = copy.deepcopy(state)
        if self.game_value(state) != 0:
            return self.game_value(state), state
        
        if depth >= 3:
            return self.heuristic_game_value(state)
        else:
            piece = self.my_piece
            a = -100     
            for s in self.succ(state, piece):
                val, ss = self.min_value(s, depth+1)               
                if val > a:
                    a = val
                    new_state = copy.deepcopy(s)              
        return a, new_state
            
    def min_value(self, state, depth):
        new_state = copy.deepcopy(state)
        if self.game_value(state) != 0:
            return self.game_value(state), state
        
        if depth >= 3:
            return self.heuristic_game_value(state)
        else:
            piece = self.opp
            a =100
            for s in self.succ(state, piece):
                val, ss = self.max_value(s, depth+1)
                if val< a:
                    a = val
                    new_state = copy.deepcopy(s)           
        return a, new_state    
        
    def make_move(self, state):
        """ Selects a (row, col) space for the next move. You may assume that whenever
        this function is called, it is this player's turn to move.

        Args:
            state (list of lists): should be the current state of the game as saved in
                this TeekoPlayer object. Note that this is NOT assumed to be a copy of
                the game state and should NOT be modified within this method (use
                place_piece() instead). Any modifications (e.g. to generate successors)
                should be done on a deep copy of the state.

                In the "drop phase", the state will contain less than 8 elements which
                are not ' ' (a single space character).

        Return:
            move (list): a list of move tuples such that its format is
                    [(row, col), (source_row, source_col)]
                where the (row, col) tuple is the location to place a piece and the
                optional (source_row, source_col) tuple contains the location of the
                piece the AI plans to relocate (for moves after the drop phase). In
                the drop phase, this list should contain ONLY THE FIRST tuple.

        Note that without drop phase behavior, the AI will just keep placing new markers
            and will eventually take over the board. This is not a valid strategy and
            will earn you no points.
        """

        drop_phase = True  # TODO: detect drop phase
        count_pieces = 0
        for r in state:
            for c in r:
                if c != ' ':
                    count_pieces += 1
        
        if count_pieces < 8:
            drop_phase = True
        else:
            drop_phase = False
        
        move = []
        if not drop_phase:
            # TODO: choose a piece to move and remove it from the board
            # (You may move this condition anywhere, just be sure to handle it)
            #
            # Until this part is implemented and the move list is updated
            # accordingly, the AI will not follow the rules after the drop phase!
            value, new_state = self.max_value(state, 0)
            for r in range(5):
                for c in range(5):
                    if state[r][c] != new_state[r][c]:
                        if state[r][c] == ' ':
                            move.insert(0,(r,c))
                        else:
                            move.insert(1,(r,c))
                            
            return move

        # select an unoccupied space randomly
        # TODO: implement a minimax algorithm to play better
        
        #(row, col) = (random.randint(0, 4), random.randint(0, 4))
        #while not state[row][col] == ' ':
        #    (row, col) = (random.randint(0, 4), random.randint(0, 4))

        # ensure the destination (row,col) tuple is at the beginning of the move list
        #move.insert(0, (row, col))
        value, new_state = self.max_value(state, 0)
        for r in range(5):
            for c in range(5):
                if state[r][c] != new_state[r][c]:
                    if state[r][c] == ' ':
                        move.insert(0,(r,c))                      
       
        return move
    
            
    
    def opponent_move(self, move):
        """ Validates the opponent's next move against the internal board representation.
        You don't need to touch this code.

        Args:
            move (list): a list of move tuples such that its format is
                    [(row, col), (source_row, source_col)]
                where the (row, col) tuple is the location to place a piece and the
                optional (source_row, source_col) tuple contains the location of the
                piece the AI plans to relocate (for moves after the drop phase). In
                the drop phase, this list should contain ONLY THE FIRST tuple.
        """
        # validate input
        if len(move) > 1:
            source_row = move[1][0]
            source_col = move[1][1]
            if source_row != None and self.board[source_row][source_col] != self.opp:
                self.print_board()
                print(move)
                raise Exception("You don't have a piece there!")
            if abs(source_row - move[0][0]) > 1 or abs(source_col - move[0][1]) > 1:
                self.print_board()
                print(move)
                raise Exception('Illegal move: Can only move to an adjacent space')
        if self.board[move[0][0]][move[0][1]] != ' ':
            raise Exception("Illegal move detected")
        # make move
        self.place_piece(move, self.opp)

    def place_piece(self, move, piece):
        """ Modifies the board representation using the specified move and piece

        Args:
            move (list): a list of move tuples such that its format is
                    [(row, col), (source_row, source_col)]
                where the (row, col) tuple is the location to place a piece and the
                optional (source_row, source_col) tuple contains the location of the
                piece the AI plans to relocate (for moves after the drop phase). In
                the drop phase, this list should contain ONLY THE FIRST tuple.

                This argument is assumed to have been validated before this method
                is called.
            piece (str): the piece ('b' or 'r') to place on the board
        """
        if len(move) > 1:
            self.board[move[1][0]][move[1][1]] = ' '
        self.board[move[0][0]][move[0][1]] = piece

    def print_board(self):
        """ Formatted printing for the board """
        for row in range(len(self.board)):
            line = str(row) + ": "
            for cell in self.board[row]:
                line += cell + " "
            print(line)
        print("   A B C D E")

    def game_value(self, state):
        """ Checks the current board status for a win condition

        Args:
        state (list of lists): either the current state of the game as saved in
            this TeekoPlayer object, or a generated successor state.

        Returns:
            int: 1 if this TeekoPlayer wins, -1 if the opponent wins, 0 if no winner

        TODO: complete checks for diagonal and box wins
        """
        # check horizontal wins
        for row in state:
            for i in range(2):
                if row[i] != ' ' and row[i] == row[i + 1] == row[i + 2] == row[i + 3]:
                    return 1 if row[i] == self.my_piece else -1

        # check vertical wins
        for col in range(5):
            for i in range(2):
                if state[i][col] != ' ' and state[i][col] == state[i + 1][col] == state[i + 2][col] == state[i + 3][col]:
                    return 1 if state[i][col] == self.my_piece else -1

        # TODO: check \ diagonal wins
        for r in range(2):
            for c in range(2):
                if state[r][c] != ' ' and state[r][c] == state[r+1][c+1] == state[r+2][c+2] == state[r+3][c+3]:
                    return 1 if state[r][c] == self.my_piece else -1
        # TODO: check / diagonal wins
        for r in range(3,5):
            for c in range(2):
                if state[r][c] != ' ' and state[r][c] == state[r-1][c+1] == state[r-2][c+2] == state[r-3][c+3]:
                    return 1 if state[r][c] == self.my_piece else -1
        # TODO: check box wins
        for r in range(4):
            for c in range(4):
                if state[r][c] != ' ' and state[r][c] == state[r+1][c] == state[r][c+1] == state[r+1][c+1]:
                    return 1 if state[r][c] == self.my_piece else -1
        
        return 0  # no winner yet


############################################################################
#
# THE FOLLOWING CODE IS FOR SAMPLE GAMEPLAY ONLY
#
############################################################################
def main():
    print('Hello, this is Samaritan')
    ai = TeekoPlayer()
    piece_count = 0
    turn = 0

    # drop phase
    while piece_count < 8 and ai.game_value(ai.board) == 0:

        # get the player or AI's move
        if ai.my_piece == ai.pieces[turn]:
            ai.print_board()
            move = ai.make_move(ai.board)
            ai.place_piece(move, ai.my_piece)
            print(ai.my_piece + " moved at " + chr(move[0][1] + ord("A")) + str(move[0][0]))
        else:
            move_made = False
            ai.print_board()
            print(ai.opp + "'s turn")
            while not move_made:
                player_move = input("Move (e.g. B3): ")
                while player_move[0] not in "ABCDE" or player_move[1] not in "01234":
                    player_move = input("Move (e.g. B3): ")
                try:
                    ai.opponent_move([(int(player_move[1]), ord(player_move[0]) - ord("A"))])
                    move_made = True
                except Exception as e:
                    print(e)

        # update the game variables
        piece_count += 1
        turn += 1
        turn %= 2

    # move phase - can't have a winner until all 8 pieces are on the board
    while ai.game_value(ai.board) == 0:

        # get the player or AI's move
        if ai.my_piece == ai.pieces[turn]:
            ai.print_board()
            move = ai.make_move(ai.board)
            ai.place_piece(move, ai.my_piece)
            print(ai.my_piece + " moved from " + chr(move[1][1] + ord("A")) + str(move[1][0]))
            print("  to " + chr(move[0][1] + ord("A")) + str(move[0][0]))
        else:
            move_made = False
            ai.print_board()
            print(ai.opp + "'s turn")
            while not move_made:
                move_from = input("Move from (e.g. B3): ")
                while move_from[0] not in "ABCDE" or move_from[1] not in "01234":
                    move_from = input("Move from (e.g. B3): ")
                move_to = input("Move to (e.g. B3): ")
                while move_to[0] not in "ABCDE" or move_to[1] not in "01234":
                    move_to = input("Move to (e.g. B3): ")
                try:
                    ai.opponent_move([(int(move_to[1]), ord(move_to[0]) - ord("A")),
                                      (int(move_from[1]), ord(move_from[0]) - ord("A"))])
                    move_made = True
                except Exception as e:
                    print(e)

        # update the game variables
        turn += 1
        turn %= 2

    ai.print_board()
    if ai.game_value(ai.board) == 1:
        print("AI wins! Game over.")
    else:
        print("You win! Game over.")


if __name__ == "__main__":
    main()
