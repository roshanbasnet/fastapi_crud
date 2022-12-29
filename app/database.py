from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings

# SQLALCHEMY_DATABASE_URL = "postgresql://<username>:<password>@<ip address/host name>/<database>/"
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

# engine establishes connection with database
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# DB connection for postgresql
# while True:
#     try:
#         conn = psycopg2.connect(host="localhost",
#                                 database="fastapi",
#                                 user="postgres",
#                                 password="root",
#                                 cursor_factory=RealDictCursor)

#         # to execute the query
#         cursor = conn.cursor()
#         print("connected to database")

#         break

#     except Exception as error:
#         print("Error while connecting to database", error)
#         time.sleep(2)
