import argparse

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import ObjectProperty

from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout

# Implicitly used widgets need to be exposed.
from desk_clock.chronometer import Chronometer
from desk_clock.calendar import Calendar


class DeskClock(GridLayout):
    chronometer = ObjectProperty(None)
    calendar = ObjectProperty(None)

    def build(self):
        self.calendar.today()

    def update(self, dt):
        self.chronometer.update(dt)


class DeskClockApp(App):
    def build(self):
        desk_clock = DeskClock()
        desk_clock.build()
        Clock.schedule_interval(desk_clock.update, 0.5)
        return desk_clock


def parse_command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--show-cursor', 
        action='store_true', 
        help='Show cursor in window (useful for non-touchscreens)'
    )

    args = parser.parse_args()
    return args
    
def main():
    args = parse_command_line()
    Window.show_cursor = args.show_cursor
    DeskClockApp().run()

if __name__ == '__main__':
    main()