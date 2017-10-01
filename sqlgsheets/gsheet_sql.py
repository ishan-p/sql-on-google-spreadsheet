from .sql_handler import SQLHandler


class GsheetSQL(object):
    
    def __init__(self):
        pass

    def select(self, table, columns=[], aliases=[], where=[], agg=[], group_by=[], having=[]):
        df = table.dataframe
        sql_handler = SQLHandler()
        sql_result = sql_handler.select(df, columns, aliases, where, agg, group_by, having)
        return sql_result.values.tolist()
