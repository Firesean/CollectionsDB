from cardData import *


class DataBases:

    DOUBLE_QUOTE = "\""
    SEMI_COLON = ";"
    SEPARATOR = ", "
    SINGLE_QUOTE = r"'"

    @staticmethod
    def enclose(string, enclose_char):
        return enclose_char + string + enclose_char

    def value_data_to_insert_sql(self, table, columns, data_sets):
        columns = self.SEPARATOR.join(columns)
        sql = f"INSERT INTO {table}({columns})\n VALUES"
        for data_set in data_sets:
            for data in data_set:
                if isinstance(data, str):
                    index = data_set.index(data)
                    data = self.enclose(data, self.DOUBLE_QUOTE)
                    data_set[index] = data
            data_set = self.SEPARATOR.join(data_set)
            sql += f"({data_set})"
            sql += self.SEPARATOR
        sql = sql[:-len(self.SEPARATOR)]
        return sql + self.SEMI_COLON  # DON'T FORGET A SEMICOLON!


sql_code = DataBases().value_data_to_insert_sql("cards",
                                                ["cardName", "cardRarity",
                                                 "cardCondition", "cardGame",
                                                 "cardLocation"],
                                                vanilla_box)
try:
    f = open("sqlCode.sql", "x")
    f.close()
except IOError:
    pass
finally:
    with open("sqlCode.sql", "r+") as f:
        f.write(sql_code)


quit()
