import numpy as np

class general_object():
    def __init__(self, x=0, y=0, v=0, direc=0):
        self.x = x
        self.y = y
        self._v = v
        self._dire = direc

    def step(self):
        self.x += self._v * np.cos(self._dire)
        self.y += self._v * np.sin(self._dire)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.x, self.y, self._v, self._dire})'

    def __str__(self):
        return f'position: {(self.x, self.y)}\nvelocity: {(self._v, self._dire)}'
    

class space_ship(general_object):
    def __init__ (self, x=0, y=0, v=0, direc=0):
        super().__init__(x, y, v, direc)
        self.__sensib_direc = 10
        self.__sensib_v = 1

    def turn_rigth(self):
        self._dire += self.__sensib_direc

    def turn_left(self):
        self._dire -= self.__sensib_direc

    def incr_vel(self):
        self._v += self.__sensib_v

    def decr_vel(self):
        self._v -= self.__sensib_v

        
    