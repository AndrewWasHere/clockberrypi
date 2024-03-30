import calendar
import datetime

from kivy.logger import Logger
from kivy.properties import (
    NumericProperty,
    ObjectProperty,
    StringProperty
)
from kivy.uix.boxlayout import BoxLayout


class Calendar(BoxLayout):
    cal = StringProperty()
    year = NumericProperty()
    month = NumericProperty()

    def update(self):
        c = calendar.TextCalendar()
        self.cal = c.formatmonth(self.year, self.month)

    def previous(self):
        Logger.info('Calendar: previous')
        self.month -= 1
        if self.month < 1:
            self.year -= 1
            self.month = 12

        self.update()

    def next(self):
        Logger.info('Calendar: next')
        self.month += 1
        if self.month > 12:
            self.year += 1
            self.month = 1

        self.update()

    def today(self):
        Logger.info('Calendar: today')
        today = datetime.date.today()
        self.year = today.year
        self.month = today.month
        self.update()
