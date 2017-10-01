import pandas as pd
import numpy as np


class SQLHandler(object):

    def __init__(self):
        pass

    def __parse_equation(self, df, lhs, operator, rhs):
        if operator == 'eq':
            return df[df[lhs] == rhs]
        elif operator == 'neq':
            return df[df[lhs] != rhs]
        elif operator == 'gt':
            return df[df[lhs] > rhs]
        elif operator == 'gteq':
            return df[df[lhs] >= rhs]
        elif operator == 'lt':
            return df[df[lhs] < rhs]
        elif operator == 'lteq':
            return df[df[lhs] <= rhs]
        elif operator == 'like':
            return df[df[lhs].str.contains(rhs)]
        elif operator == 'not like':
            return df[~df[lhs].str.contains(rhs)]
        elif operator == 'in':
            return df[df.lhs.isin(rhs)]
        elif operator == 'not in':
            return df[~df.lhs.isin(rhs)]
        elif operator == 'is null':
            return df[df[lhs].isnull()]
        elif operator == 'is not null':
            return df[df[lhs].notnull()]

    def __parse_where(self, df, where):
        temp_state = df
        itr = 1
        for clause in where:
            if len(clause) != 1:
                temp_state = self.__parse_where(temp_state, clause)
            if itr == 1 and not clause[0][0]:
                temp_state = self.__parse_equation(df, clause[0][1], clause[0][2], clause[0][3])
            elif clause[0][0] == 'and':
                temp_state = self.__parse_equation(temp_state, clause[0][1], clause[0][2], clause[0][3])
            elif clause[0][0] == 'or':
                temp = self.__parse_equation(df, clause[0][1], clause[0][2], clause[0][3])
                temp_state = pd.concat([temp_state, temp])
                temp_state = temp_state.drop_duplicates()
            itr = itr + 1
        return temp_state

    def select(self, df, columns=[], aliases=[], where=[], agg=[], group_by=[], having=[]):
        temp = self.__parse_where(df, where)
        result = pd.DataFrame()
        if columns:
            for column in columns:
                result[column] = temp[column]
        else:
            result = temp
        return result
