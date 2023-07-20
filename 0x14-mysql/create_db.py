import mysql.connector

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "0700479408"
DB_NAME = "tyrell_corp"

def create_database():
    """Creates the tyrell_corp database."""

    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
    )
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(DB_NAME))

def create_table():
    """Creates the nexus6 table in the tyrell_corp database."""

    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
    )
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE nexus6 (
            id INT NOT NULL AUTO_INCREMENT,
            serial_number VARCHAR(255) NOT NULL,
            model_number VARCHAR(255) NOT NULL,
            created_at DATETIME NOT NULL,
            updated_at DATETIME NOT NULL,
            PRIMARY KEY (id)
        )
    """)

def grant_permissions():
    """Grants SELECT permissions to the holberton_user on the nexus6 table."""

    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
    )
    cursor = connection.cursor()
    cursor.execute("""
        GRANT SELECT ON nexus6 TO holberton_user;
    """)

def main():
    create_database()
    create_table()
    grant_permissions()

if __name__ == "__main__":
    main()
