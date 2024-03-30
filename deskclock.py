from kivy.app import App
from kivy.clock import Clock
from kivy.properties import ObjectProperty

from desk_clock.chronometer import Chronometer
from kivy.uix.widget import Widget


class DeskClock(Widget):
    chronometer = ObjectProperty(None)

    def update(self, dt):
        self.chronometer.update(dt)

class DeskClockApp(App):
    def build(self):
        desk_clock = DeskClock()
        Clock.schedule_interval(desk_clock.update, 0.5)
        return desk_clock
        
    
if __name__ == '__main__':
    DeskClockApp().run()
