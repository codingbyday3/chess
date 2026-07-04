
class Pawn:

    def __init__(self, player,  board, starting_x, starting_y):
        self.board = board
        self.player = player
        self.starting_x = starting_x
        self.starting_y = starting_y

    def valid_moves(self, x, y):
        #white player
        if self.player == '1' :
            #forward movement
            if self.board[y][x] == '':
                if y == self.starting_y - 2 and self.starting_y == 6:
                    return True
                elif y == self.starting_y - 1:
                    return True
                else:
                    return False
            #sideways movement
            elif self.board[y][x] != '' and self.board[y][x][0] != '1':
                if y == self.starting_y - 1 and x == self.starting_x + 1:
                    return True
                elif y == self.starting_y - 1 and x == self.starting_x - 1:
                    return True
                else:
                    return False
        #black player
        if self.player == '2' :
            #forward movement
            if self.board[y][x] == '':
                if y == self.starting_y + 2 and self.starting_y == 1:
                    return True
                elif y == self.starting_y + 1:
                    return True
                else:
                    return False
            #sideways movement
            elif self.board[y][x] != '' and self.board[y][x][0] != '2':
                if y == self.starting_y + 1 and x == self.starting_x + 1:
                    return True
                elif y == self.starting_y + 1 and x == self.starting_x - 1:
                    return True
                else:
                    return False
    


class Knight:

    def __init__(self, player,  board, starting_x, starting_y):
        self.board = board
        self.player = player
        self.starting_x = starting_x
        self.starting_y = starting_y
    
    def valid_moves(self, x, y):
        #moving forward
        if self.board[y][x] == '' or self.board[y][x][0] != self.player:
            if y == self.starting_y - 2 and x == self.starting_x + 1:
                return True
            elif y == self.starting_y - 2 and x == self.starting_x - 1:
                return True
            
            #moving sideways
            elif y == self.starting_y - 1 and x == self.starting_x + 2:
                return True
            elif y == self.starting_y + 1 and x == self.starting_x + 2:
                return True
            
            elif y == self.starting_y - 1 and x == self.starting_x - 2:
                return True
            elif y == self.starting_y + 1 and x == self.starting_x - 2:
                return True
            
            #moving downwards
            elif y == self.starting_y + 2 and x == self.starting_x + 1:
                return True
            elif y == self.starting_y + 2 and x == self.starting_x - 1:
                return True
        
        return False
    

class Bishop:
    def __init__(self, player,  board, starting_x, starting_y):
        self.board = board
        self.player = player
        self.starting_x = starting_x
        self.starting_y = starting_y
    
    def valid_moves(self, x, y):
        #moving downwards-right
        for i in range(1, 8):
            check_poition_x = self.starting_x + i
            check_poition_y = self.starting_y + i
            
            if check_poition_x <= 7 and check_poition_x >= 0 and check_poition_y <= 7 and check_poition_y >= 0:
                if self.board[check_poition_y][check_poition_x] != '' and self.board[check_poition_y][check_poition_x][0] != self.player:
                    if x == check_poition_x and y == check_poition_y:
                        return True
                    else:
                        break
                elif self.board[check_poition_y][check_poition_x] != '':
                    break
                elif x == check_poition_x and y == check_poition_y:
                    return True
                else:
                    continue
            else:
                break

        #moving downwards-left
        for i in range(1, 8):
            check_poition_x = self.starting_x - i
            check_poition_y = self.starting_y + i
            
            if check_poition_x <= 7 and check_poition_x >= 0 and check_poition_y <= 7 and check_poition_y >= 0:
                if self.board[check_poition_y][check_poition_x] != '' and self.board[check_poition_y][check_poition_x][0] != self.player:
                    if x == check_poition_x and y == check_poition_y:
                        return True
                    else:
                        break
                elif self.board[check_poition_y][check_poition_x] != '':
                    break
                elif x == check_poition_x and y == check_poition_y:
                    return True
                else:
                    continue
            else:
               break

        #moving forward-right
        for i in range(1, 8):
            check_poition_x = self.starting_x + i
            check_poition_y = self.starting_y - i
            
            if check_poition_x <= 7 and check_poition_x >= 0 and check_poition_y <= 7 and check_poition_y >= 0:
                if self.board[check_poition_y][check_poition_x] != '' and self.board[check_poition_y][check_poition_x][0] != self.player:
                    if x == check_poition_x and y == check_poition_y:
                        return True
                    else:
                        break
                elif self.board[check_poition_y][check_poition_x] != '':
                    break
                elif x == check_poition_x and y == check_poition_y:
                    return True
                else:
                    continue
            else:
                break
            
        #moving forward-left
        for i in range(1, 8):
            check_poition_x = self.starting_x - i
            check_poition_y = self.starting_y - i
            
            if check_poition_x <= 7 and check_poition_x >= 0 and check_poition_y <= 7 and check_poition_y >= 0:
                if self.board[check_poition_y][check_poition_x] != '' and self.board[check_poition_y][check_poition_x][0] != self.player:
                    if x == check_poition_x and y == check_poition_y:
                        return True
                    else:
                        break
                elif self.board[check_poition_y][check_poition_x] != '':
                    break
                elif x == check_poition_x and y == check_poition_y:
                    return True
                else:
                    continue
            else:
                break
        
        return False

class Rook:
    def __init__(self, player,  board, starting_x, starting_y):
        self.board = board
        self.player = player
        self.starting_x = starting_x
        self.starting_y = starting_y
    
    def valid_moves(self, x, y):
        #moving forward
        for i in range(1, 8):

            check_poition_x = self.starting_x
            check_poition_y = self.starting_y - i
            
            if check_poition_x <= 7 and check_poition_x >= 0 and check_poition_y <= 7 and check_poition_y >= 0:
                if self.board[check_poition_y][check_poition_x] != '' and self.board[check_poition_y][check_poition_x][0] != self.player:
                    if x == check_poition_x and y == check_poition_y:
                        return True
                    else:
                        break
                elif self.board[check_poition_y][check_poition_x] != '':
                    break
                elif x == check_poition_x and y == check_poition_y:
                    return True
                else:
                    continue
            else:
                break

        #moving right
        for i in range(1, 8):
            check_poition_x = self.starting_x + i
            check_poition_y = self.starting_y
            
            if check_poition_x <= 7 and check_poition_x >= 0 and check_poition_y <= 7 and check_poition_y >= 0:
                if self.board[check_poition_y][check_poition_x] != '' and self.board[check_poition_y][check_poition_x][0] != self.player:
                    if x == check_poition_x and y == check_poition_y:
                        return True
                    else:
                        break
                elif self.board[check_poition_y][check_poition_x] != '':
                    break
                elif x == check_poition_x and y == check_poition_y:
                    return True
                else:
                    continue
            else:
               break

        #moving left
        for i in range(1, 8):
            check_poition_x = self.starting_x - i
            check_poition_y = self.starting_y
            
            if check_poition_x <= 7 and check_poition_x >= 0 and check_poition_y <= 7 and check_poition_y >= 0:
                if self.board[check_poition_y][check_poition_x] != '' and self.board[check_poition_y][check_poition_x][0] != self.player:
                    if x == check_poition_x and y == check_poition_y:
                        return True
                    else:
                        break
                elif self.board[check_poition_y][check_poition_x] != '':
                    break
                elif x == check_poition_x and y == check_poition_y:
                    return True
                else:
                    continue
            else:
                break
            
        #moving downwards
        for i in range(1, 8):

            check_poition_x = self.starting_x
            check_poition_y = self.starting_y + i

            
            if check_poition_x <= 7 and check_poition_x >= 0 and check_poition_y <= 7 and check_poition_y >= 0:
                if self.board[check_poition_y][check_poition_x] != '' and self.board[check_poition_y][check_poition_x][0] != self.player:
                    if x == check_poition_x and y == check_poition_y:
                        return True
                    else:
                        break
                elif self.board[check_poition_y][check_poition_x] != '':
                    break
                elif x == check_poition_x and y == check_poition_y:
                    return True
                else:
                    continue
            else:
                break
        
        return False
    

class Queen:
    def __init__(self, player,  board, starting_x, starting_y):
        self.board = board
        self.player = player
        self.starting_x = starting_x
        self.starting_y = starting_y
    
    def valid_moves(self, x, y):
        #moving forward
        for i in range(1, 8):

            check_poition_x = self.starting_x
            check_poition_y = self.starting_y - i
            
            if check_poition_x <= 7 and check_poition_x >= 0 and check_poition_y <= 7 and check_poition_y >= 0:
                if self.board[check_poition_y][check_poition_x] != '' and self.board[check_poition_y][check_poition_x][0] != self.player:
                    if x == check_poition_x and y == check_poition_y:
                        return True
                    else:
                        break
                elif self.board[check_poition_y][check_poition_x] != '':
                    break
                elif x == check_poition_x and y == check_poition_y:
                    return True
                else:
                    continue
            else:
                break

        #moving right
        for i in range(1, 8):
            check_poition_x = self.starting_x + i
            check_poition_y = self.starting_y
            
            if check_poition_x <= 7 and check_poition_x >= 0 and check_poition_y <= 7 and check_poition_y >= 0:
                if self.board[check_poition_y][check_poition_x] != '' and self.board[check_poition_y][check_poition_x][0] != self.player:
                    if x == check_poition_x and y == check_poition_y:
                        return True
                    else:
                        break
                elif self.board[check_poition_y][check_poition_x] != '':
                    break
                elif x == check_poition_x and y == check_poition_y:
                    return True
                else:
                    continue
            else:
               break

        #moving left
        for i in range(1, 8):
            check_poition_x = self.starting_x - i
            check_poition_y = self.starting_y
            
            if check_poition_x <= 7 and check_poition_x >= 0 and check_poition_y <= 7 and check_poition_y >= 0:
                if self.board[check_poition_y][check_poition_x] != '' and self.board[check_poition_y][check_poition_x][0] != self.player:
                    if x == check_poition_x and y == check_poition_y:
                        return True
                    else:
                        break
                elif self.board[check_poition_y][check_poition_x] != '':
                    break
                elif x == check_poition_x and y == check_poition_y:
                    return True
                else:
                    continue
            else:
                break
            
        #moving downwards
        for i in range(1, 8):

            check_poition_x = self.starting_x
            check_poition_y = self.starting_y + i

            
            if check_poition_x <= 7 and check_poition_x >= 0 and check_poition_y <= 7 and check_poition_y >= 0:
                if self.board[check_poition_y][check_poition_x] != '' and self.board[check_poition_y][check_poition_x][0] != self.player:
                    if x == check_poition_x and y == check_poition_y:
                        return True
                    else:
                        break
                elif self.board[check_poition_y][check_poition_x] != '':
                    break
                elif x == check_poition_x and y == check_poition_y:
                    return True
                else:
                    continue
            else:
                break
        
        #moving downwards-right
        for i in range(1, 8):
            check_poition_x = self.starting_x + i
            check_poition_y = self.starting_y + i
            
            if check_poition_x <= 7 and check_poition_x >= 0 and check_poition_y <= 7 and check_poition_y >= 0:
                if self.board[check_poition_y][check_poition_x] != '' and self.board[check_poition_y][check_poition_x][0] != self.player:
                    if x == check_poition_x and y == check_poition_y:
                        return True
                    else:
                        break
                elif self.board[check_poition_y][check_poition_x] != '':
                    break
                elif x == check_poition_x and y == check_poition_y:
                    return True
                else:
                    continue
            else:
                break

        #moving downwards-left
        for i in range(1, 8):
            check_poition_x = self.starting_x - i
            check_poition_y = self.starting_y + i
            
            if check_poition_x <= 7 and check_poition_x >= 0 and check_poition_y <= 7 and check_poition_y >= 0:
                if self.board[check_poition_y][check_poition_x] != '' and self.board[check_poition_y][check_poition_x][0] != self.player:
                    if x == check_poition_x and y == check_poition_y:
                        return True
                    else:
                        break
                elif self.board[check_poition_y][check_poition_x] != '':
                    break
                elif x == check_poition_x and y == check_poition_y:
                    return True
                else:
                    continue
            else:
               break

        #moving forward-right
        for i in range(1, 8):
            check_poition_x = self.starting_x + i
            check_poition_y = self.starting_y - i
            
            if check_poition_x <= 7 and check_poition_x >= 0 and check_poition_y <= 7 and check_poition_y >= 0:
                if self.board[check_poition_y][check_poition_x] != '' and self.board[check_poition_y][check_poition_x][0] != self.player:
                    if x == check_poition_x and y == check_poition_y:
                        return True
                    else:
                        break
                elif self.board[check_poition_y][check_poition_x] != '':
                    break
                elif x == check_poition_x and y == check_poition_y:
                    return True
                else:
                    continue
            else:
                break
            
        #moving forward-left
        for i in range(1, 8):
            check_poition_x = self.starting_x - i
            check_poition_y = self.starting_y - i
            
            if check_poition_x <= 7 and check_poition_x >= 0 and check_poition_y <= 7 and check_poition_y >= 0:
                if self.board[check_poition_y][check_poition_x] != '' and self.board[check_poition_y][check_poition_x][0] != self.player:
                    if x == check_poition_x and y == check_poition_y:
                        return True
                    else:
                        break
                elif self.board[check_poition_y][check_poition_x] != '':
                    break
                elif x == check_poition_x and y == check_poition_y:
                    return True
                else:
                    continue
            else:
                break
        
        return False
    

class King:
    def __init__(self, player,  board, starting_x, starting_y):
        self.board = board
        self.player = player
        self.starting_x = starting_x
        self.starting_y = starting_y

    def valid_moves(self, x, y):
        #moving forward
        if self.board[y][x] == '' or self.board[y][x][0] != self.player:
            if y == self.starting_y - 1 and x == self.starting_x:
                return True
            
            #moving down
            elif y == self.starting_y + 1 and x == self.starting_x:
                return True
            
            #moving right
            elif y == self.starting_y and x == self.starting_x + 1:
                return True
            
            #moving left
            elif y == self.starting_y and x == self.starting_x - 1:
                return True
            #moving down-right
            elif y == self.starting_y + 1 and x == self.starting_x + 1:
                return True
            
            #moving down-left
            elif y == self.starting_y + 1 and x == self.starting_x - 1:
                return True
            
            #moving top-right
            elif y == self.starting_y - 1 and x == self.starting_x + 1:
                return True
            
            #moving top-left
            elif y == self.starting_y - 1 and x == self.starting_x - 1:
                return True
        
        return False