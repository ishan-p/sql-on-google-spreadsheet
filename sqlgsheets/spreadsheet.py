import pygsheets

from .worksheet import Worksheet


class Spreadsheet(object):

    def __init__(self, title, secret_file):
        gc = pygsheets.authorize(service_file=secret_file)
        self.spreadsheet = gc.open(title)

    def worksheet(self, title):
        return Worksheet(self.spreadsheet, title)
