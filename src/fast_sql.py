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
        # Import library
        import sqlite3 as sql
        # Create values
        connect = sql.connect(db_name)
        cursor = connect.cursor()
        str_attributes = convert_attr_to_text(attributes)
        # Create Table in database
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} ({str_attributes});""")
        # Commit changes
        connect.commit()
        # Create self values
        self.db_name = db_name
        self.tb_name = table_name
        self.attributes = attributes
        self.sql = sql
        self.con = connect
        self.cursor = cursor
        self.str_attributes = str_attributes
    def Insert_in(self, values: list):
        if len(self.attributes) != len(values):
            return "Error; Len of attributes not equal to values len. Please check it."
        else: 
            values = convert_attr_to_text(values)
            self.cursor.execute(f"""INSERT INTO {self.tb_name} ({self.str_attributes})
                                VALUES ({values})""")
            self.con.commit()
            return True
    def __close__(self):
        try: 
            self.con.close()
            return True
        except: 
            return False
