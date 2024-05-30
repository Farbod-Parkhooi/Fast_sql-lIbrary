def convert_attr_to_text(attributes):
    output = "" 
    num = len(attributes)-1 
    # convert attributes to text
    for i in range(len(attributes)):
        output += f"'{attributes[i]}"
        if i >= num: output += "'"
        else: output += "', "
    return output
class fast_sql():
    def __init__(self, db_name: str, table_name: str, attributes: list):
        # Create self values
        self.db_name = db_name
        self.tb_name = table_name
        self.attributes = attributes
    def connect(self):
        # Import library
        import sqlite3 as sql
        # Create values
        connect = sql.connect(self.db_name)
        cursor = connect.cursor()
        str_attributes = convert_attr_to_text(self.attributes)
        # Create Table in database
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {self.tb_name} ({str_attributes});""")
        # Commit changes
        connect.commit()
        # add more self values
        self.sql = sql
        self.con = connect
        self.cursor = cursor
        self.str_attributes = str_attributes
    def close(self):
        try: 
            self.con.close()
            return True
        except: 
            return False
    def Insert_in(self, values: list):
        if len(self.attributes) != len(values):
            return "Error; Len of attributes not equal to values len. Please check it."
        else: 
            values = convert_attr_to_text(values)
            self.cursor.execute(f"""INSERT INTO {self.tb_name} ({self.str_attributes})
                                VALUES ({values});""")
            self.con.commit()
            return True
    def Select_from(self, Select: str, Where_value: str, input: str): 
        self.cursor.execute(f"""SELECT {Select} FROM {self.tb_name} WHERE {Where_value}='{input}';""")
        return self.cursor.fetchall()
    def Custome_command(self, command):
        self.cursor.execute(command)
        return self.cursor.fetchall()
    def add_new_column(self, column_name: str):
        self.cursor.execute(f"""ALTER TABLE {self.tb_name} ADD COLUMN {column_name};""")
        self.con.commit()
        return True
    def remove_column(self, column_name: str):
        self.cursor.execute(f"""ALTER TABLE {self.tb_name} DROP COLUMN {column_name};""")
        self.con.commit()
        return True
    def all_table_data(self):
        self.cursor.execute(f"""SELECT * FROM {self.tb_name};""")
        return self.cursor.fetchall()
    def all_rows(self):
        self.cursor.execute(f"""SELECT COUNT (*) FROM {self.tb_name};""")
        return self.cursor.fetchall()
    def clear_table(self):
        self.cursor.execute(f"""DELETE FROM {self.tb_name};""")
        self.con.commit()
        return True
