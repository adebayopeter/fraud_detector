import os
from sqlpyhelper.db_helper import SQLPyHelper


def run_schema():
    with open("db/schema.sql", "r") as f:
        sql_script = f.read()

    db = SQLPyHelper()
    db.execute_query(sql_script)


if __name__ == "__main__":
    run_schema()
    print("✅ Database schema applied.")
