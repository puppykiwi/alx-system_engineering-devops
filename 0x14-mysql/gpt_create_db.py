from sqlalchemy import create_engine, Column, Integer, String, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import ProgrammingError

# Replace 'username' and 'password' with your MySQL username and password.
# Replace 'localhost' with your MySQL host.
db_url = 'mysql+mysqldb://root:0700479408@localhost/tyrell_corp'
engine = create_engine(db_url)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Nexus6(Base):
    __tablename__ = 'nexus6'
    id = Column(Integer, primary_key=True, autoincrement=True)
    model = Column(String(50))
    serial_number = Column(String(20))
    manufacture_date = Column(Date)
    additional_info = Column(Text)

def create_database():
    # Create the database named tyrell_corp
    engine.execute("CREATE DATABASE IF NOT EXISTS tyrell_corp")
    engine.execute("USE tyrell_corp")

def create_table():
    # Create the nexus6 table
    Base.metadata.create_all(engine)

def insert_data():
    # Insert at least one entry into the nexus6 table
    session = Session()
    nexus6_entry = Nexus6(
        model='Nexus 6',
        serial_number='NXS60001',
        manufacture_date='2023-07-20',
        additional_info='Some additional information here.'
    )
    session.add(nexus6_entry)
    session.commit()
    session.close()

def grant_permissions():
    # Grant SELECT permission on the nexus6 table to holberton_user
    try:
        engine.execute("GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost'")
    except ProgrammingError as e:
        print("Error granting permissions:", e)

if __name__ == "__main__":
    create_database()
    create_table()
    insert_data()
    grant_permissions()
