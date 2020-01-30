from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector
from kivy.core.window import Window

class AsteroidsBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class AsteroidsGame(Widget):
    player = ObjectProperty(None)

    
    def init(self):
        self.player.center
        self.player.center = self.center

# #     def update(self, dt):
# #         self.player.move()

# #     def on_touch_move(self, touch):
# #         self.player.center_x = touch.x
# #         self.player.center_y = touch.y

import tkinter

class AsteroidsApp(App):
    def build(self):
#         game = Label(text='Hello World')
#         # game = AsteroidsGame()
#         # game.init()
#         # Clock.schedule_interval(game.update, 1.0 / 60.0)
        return AsteroidsGame()

if __name__ == '__main__':
    AsteroidsApp().run()