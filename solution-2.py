
class KnightTour:
    
    def __init__(self, bd_size, s_pos):                       ## 构造函数 
        self.BDsize = bd_size                                         ## 表示棋盘的边长
        self.board = [[0]* bd_size for _ in range(bd_size )]       ## 表示棋盘，0代表未踩过，1代表踩过
        self.pathboard = [[0]* bd_size for _ in range(bd_size)]   ## 一个用来显示路径的棋盘，每个位置上的值表示它在路径上的顺序
        self.start_pos = s_pos                                  ## 表示起始点的坐标，坐标从1开始
        self.eight_dire = [[2,1],[2,-1],[-2,1],[-2,-1],         ## 定义8个方向的坐标变化
                        [1,2],[1,-2],[-1,2],[-1,-2]]

    # def FindMoves(self, cur_pos)                            ## 找出当前位置的下一步可能方向
    # def searchNext(self, cur_pos,cnt)                       ## 从当前位置开始，递归地找出路径
    # def tour(self)                                          ## 调用SearchNext计算出起始位置路径，并打印出来
    # def printBD(self, board)                                   ## 美观地打印出棋盘
    
    
    def FindMoves(self, cur_pos):
        ## 所有八个方向
        moves = [[x + y for x,y in zip(cur_pos,dire)] for dire in self.eight_dire]
        ## 八个方向中下一步可以走的方向
        valid_moves = [move for move in moves if 0<=move[0]<self.BDsize
                        and 0<=move[1]<self.BDsize
                        and self.board[move[0]][move[1]] == 0]
        return valid_moves
    
    # def searchNext(self, cur_pos, cnt):
    #     ## 在表示路径的棋盘上标上当前是第几步
    #     self.pathboard[cur_pos[0]][cur_pos[1]] = self.BDsize *self.BDsize-cnt    
    #     if cnt == 0:
    #         return True
    #     else:
    #         moves = self.FindMoves(cur_pos)
    #         if len(moves) == 0 :
    #             return False
    #         for move in moves:
    #             self.board[move[0]][move[1]] = 1
    #             if self.searchNext(move,cnt-1):    ## 递归调用，注意参数cnt-1
    #                 return True
    #             else :
    #                 self.board[move[0]][move[1]] = 0

    def tour(self):
        cur_pos = self.start_pos
        self.board[cur_pos[0]][cur_pos[1]] = 1
        return self.searchNext(cur_pos, 1)

    def printBD(self, board):
        print("-------------------------")
        for row in board:
            for column in row:
                print(column, end='\t')
            print("")
        print("-------------------------")
        
    def printPath(self):
        self.printBD(self.board)   
         
    # Return number of next next moves
    def count_next(self, cur_pos):
        valid_moves = self.FindMoves(cur_pos)
        return len(valid_moves)
    
    def count(self, cur_pos):
        valid_moves = self.FindMoves(cur_pos)
        print(valid_moves)
        return [[self.count_next(move),move] for move in valid_moves]

    def searchNext(self, cur_pos, moveCount):
        self.board[cur_pos[0]][cur_pos[1]] = moveCount   
        if moveCount >= self.BDsize* self.BDsize:
            return True
        else:
            #Here is 3D-array like [[2, [2,3]], [3, [1,4]]]
            moves = self.count(cur_pos)
            
            moves.sort()
            if moves[0][0] == 0 and moveCount!= self.BDsize*self.BDsize -1:
                return False
            for move in moves:
                #self.board[move[1][0]][move[1][1]] = 1
                if self.searchNext(move[1], moveCount+1):
                    return True
                else :
                    self.board[cur_pos[0]][cur_pos[1]] = 0



    
KT = KnightTour(8, [0,0])       ## 建立一个8*8的棋盘，出发点设置为(0,0)
if KT.tour():                  ## 查找路径
    KT.printPath()     
else:
    print("No route")