import pygsheets
import pandas as pd
import numpy as np

from .sql_handler import SQLHandler


class Worksheet(object):

    def __init__(self, spreadsheet, title):
        self.sheet = spreadsheet.worksheet_by_title(title)
        self.dataframe = self.sheet.get_as_df()
