
class KnightTour:
    
    def __init__(self, bd_size, s_pos):                       ## 构造函数 
        self.BDsize = bd_size                                         ## 表示棋盘的边长
        self.board = [[0]* bd_size for _ in range(bd_size )]       ## 表示棋盘，0代表未踩过，1代表踩过
        #self.pathboard = [[0]* bd_size for _ in range(bd_size)]   ## 一个用来显示路径的棋盘，每个位置上的值表示它在路径上的顺序
        self.start_pos = s_pos                                  ## 表示起始点的坐标，坐标从1开始
        self.eight_dire = [[2,1],[2,-1],[-2,1],[-2,-1],         ## 定义8个方向的坐标变化
                        [1,2],[1,-2],[-1,2],[-1,-2]]

    # def FindMoves(self, cur_pos)                            ## 找出当前位置的下一步可能方向
    # def searchNext(self, cur_pos,moveCount)                       ## 从当前位置开始，递归地找出路径
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
    
    def searchNext(self, cur_pos, moveCount):
        ## 在表示路径的棋盘上标上当前是第几步
        self.board[cur_pos[0]][cur_pos[1]] = moveCount
        #print(moveCount)   
        if moveCount >= self.BDsize* self.BDsize:
            return True
  
  
        moves = self.FindMoves(cur_pos)
        if len(moves) == 0 :  
            return False
    
        for move in moves:                
            #self.board[move[0]][move[1]] = moveCount
            #print(self.board)
            #self.pathboard[move[0]][move[1]] = moveCount
            if self.searchNext(move, moveCount + 1):    ## 递归调用
                return True
            else:
                self.board[move[0]][move[1]] = 0
   

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



    
KT = KnightTour(5, [3,0])       ## 建立一个N*N的棋盘，出发点设置为(0,0)
if KT.tour(): 
    KT.printPath()
else: 
    print("No route")