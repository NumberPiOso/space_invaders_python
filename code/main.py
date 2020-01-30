from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
from kivy.clock import Clock

class AsteroidsPlayer(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class AsteroidsGame(Widget):
    player = ObjectProperty(None)

    def init(self):
        self.player.center = self.center

    def update(self, dt):
        return False

    def on_touch_move(self, touch):
        self.player.center_x = touch.x
        self.player.center_y = touch.y

class AsteriodsApp(App):
    def build(self):
        game = AsteroidsGame()
        game.init()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

if __name__ == '__main__':
    AsteriodsApp().run()