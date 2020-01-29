class general_object():
    def __init__(self, x=0, y=0, vx=0, vy=0):
        self.x = x
        self.y = y
        self._vx = vx
        self._vy = vy
    def __repr__(self):
        return f'{self.__class__.__name__}({self.x, self.y, self._vx, self._vy})'
    def __str__(self):
        return f'position: {(self.x, self.y)}\nvelocity: {(self._vx, self._vy)}'
