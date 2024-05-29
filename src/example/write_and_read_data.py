# Import Library
from fast_sql import fast_sql

# create fast_sql class value
fsql = fast_sql("database.db", "Users", ["username", "email", "password"])

# connect to database
fsql.connect()

# Create an account
fsql.Insert_in(["admin", "admin.root@admin.com", "admin"])

# Get username(admin for here)
username = input("write admin here(username): ")

# read email of your account
email_addr = fsql.Select_from("email", "username", username)

# print data
print(f"This is your email: {email_addr}")

# close connection
fsql.close()
