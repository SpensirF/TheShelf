# COMMIT INTENT: feat(server): SQLAlchemy base + initial User model

# SQLA 2.0 typed ORM
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column   
# column/SQL helpers
from sqlalchemy import String, DateTime, func                       
# to generate UUIDs for IDs
import uuid                                                         

# base class all models inherit from
class Base(DeclarativeBase):                                        
    pass
# helper to create UUID strings
def uid() -> str:                                                   
    return str(uuid.uuid4())

# example model to anchor migrations
class User(Base):                                                   
    # DB table name
    __tablename__ = "users"                                         
    # primary key column
    id: Mapped[str] = mapped_column(                                
        String(36), primary_key=True, default=uid
    )
    # unique email with index
    email: Mapped[str] = mapped_column(                             
        String(255), unique=True, index=True
    )
    # bcrypt hash (never store plain passwords)
    password_hash: Mapped[str] = mapped_column(String(255))         
    # public display name
    display_name: Mapped[str] = mapped_column(String(100))          
    # server-side timestamp
    created_at: Mapped[DateTime] = mapped_column(                   
        DateTime, server_default=func.now()
    )
