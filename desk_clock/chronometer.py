import datetime

from kivy.logger import Logger
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout


class Chronometer(BoxLayout):
    time = StringProperty()
    day = StringProperty()
    date = StringProperty()

    def update(self, _):
        now = datetime.datetime.now()
        self.time = now.strftime("%I:%M %p")
        self.day = now.strftime("%A")
        self.date = now.strftime("%d %B %Y")

        return True

