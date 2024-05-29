from fast_sql import fast_sql
fsql = fast_sql("database.db", "Users", ["username", "email", "password"])
fsql.connect()
fsql.Insert_in(["admin", "admin.root@admin.com", "admin"])
email_addr = fsql.Select_from("email", "username", "admin")
fsql.close()
