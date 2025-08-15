# builds the DB connection engine
from sqlalchemy import create_engine
# creates DB sessions for requests                     
from sqlalchemy.orm import sessionmaker 
# import our loaded env settings                 
from .config import settings                             

# create a pooled engine using the env URL
engine = create_engine(                                  
    settings.DATABASE_URL,
    # checks connections before use; avoids stale sockets
    pool_pre_ping=True,                                  
)
# factory that gives us Session objects
SessionLocal = sessionmaker(                             
    bind=engine,
    # we’ll flush explicitly on commit
    autoflush=False, 
    # we manage transactions explicitly                                    
    autocommit=False,                                    
)
