"""
  * simple go environment    rbh 2024
      ? legal moves
      ? tromp taylor score
  * allow rectangular boards
  * simple data structures 
  todo * check whether position is legal
       * put more inside Game_state ?
"""

from string import ascii_lowercase

def pad_string(s):
  return ''.join([' ' + c for c in s])

class go_board:
  BLACK, WHITE, EMPTY = 0, 1, 2
  IO_CHRS = '*o.' # characters for stone output

  def opponent(self, clr):
    assert(clr == self.BLACK or clr == self.WHITE)
    return 1 - clr

  def __init__(self, r, c):

    ### go board: r horizontal lines, c vertical lines, r*c points

    self.rows, self.cols, self.n = r, c, r * c

    def rc_point(y, x):
      return x + y * self.cols

    ### neighbors of each point

    self.nbrs = {} # dictionary:  point -> neighbors
    
    for point in range(self.n):
       self.nbrs[point] = set()

    def show_points(self):
      print('\nnames of points of the go board\n')
      for y in range(self.rows - 1, -1, -1): #print last row first
        for x in range(self.cols):
          print(f'{rc_point(y, x):3}', end='')
        print()

    for y in range(self.rows):
      for x in range(self.cols):
        p = rc_point(y,x)
        if x > 0: 
          self.nbrs[p].add( rc_point(y, x - 1) )
        if x < self.cols - 1: 
          self.nbrs[p].add( rc_point(y, x + 1) )
        if y > 0: 
          self.nbrs[p].add( rc_point(y - 1, x) )
        if y < self.rows - 1: 
          self.nbrs[p].add( rc_point(y + 1, x) )
    
    def show_nbrs(self):    
      print('\nneighbors of points of the go board\n')
      for p in self.nbrs:
        print(f'{p:2}', self.nbrs[p])

    ### stones
    self.stones = [set(), set()]

    def point_str(self, p):
      if   p in self.stones[self.BLACK]: 
        return '*'
      if   p in self.stones[self.WHITE]: 
        return 'o'
      return '.'

    def board_str(self):
      return ''.join([point_str(self,p) for p in range(self.n)])

    def show_board(self):
      bstr = board_str(self)
      print('\nthe go board\n\n    ',end='')
      print(pad_string(ascii_lowercase[0:self.cols]) + '\n')
      for y in range(self.rows - 1, -1, -1): #print last row first
        print(f'{y+1:2}' + pad_string(bstr[y*self.cols : (y + 1)*self.cols]))

    show_points(self)
    show_nbrs(self)
    self.stones[self.BLACK].add(rc_point(1, 1))
    self.stones[self.BLACK].add(rc_point(1, 2))
    self.stones[self.BLACK].add(rc_point(1, 3))
    self.stones[self.WHITE].add(rc_point(0, 0))
    show_board(self)
    print()

class go_env:
  def __init__(self, r, c):
    ge = go_board(r,c)

go_env(4,5)
