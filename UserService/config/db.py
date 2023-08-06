from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("mysql+pymsql://root@localhost:3306/ekart")

sessionLocal = sessionmaker(autocommit=False, bind=engine)
base = declarative_base()

