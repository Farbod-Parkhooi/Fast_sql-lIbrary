class fast_sql():
    def __init__(self, db_name: str, table_name: str, attributes: list):
        # Import library
        import sqlite3 as sql
        # Create values
        connect = sql.connect(db_name)
        cursor = connect.cursor()
        str_attributes = "" 
        num = len(attributes)-1 
        # convert attributes to text
        for i in range(len(attributes)):
            str_attributes += f"'{attributes[i]}"
            if i >= num: str_attributes += "'"
            else: str_attributes += "', "
        # Create Table in database
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} ({str_attributes});""")
        # Commit changes
        connect.commit()
        # Close connection
        connect.close()
        # Create self values
        self.db_name = db_name
        self.tb_name = table_name
        self.attributes = attributes
        self.sql = sql
        self.con = connect
        self.cursor = cursor
        self.str_attributes = str_attributes
